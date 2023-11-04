"""
Basic sequencer nodes.

These are generic nodes that can be used as a base to construct more
complex behavior.
"""

# Libraries and Core Files
import logging
from collections.abc import Callable
from typing import Any, Self

from engine.blackboard import blackboard

logger = logging.getLogger(__name__)


class SeqBase:
    """Base node for sequencer. All nodes should inherit from `SeqBase`."""

    def __init__(self: Self, name: str = "", func: Callable = None) -> None:
        self.name = name
        self.func = func

    def reset(self: Self) -> None:
        """Reset node. Override to implement node-specific behavior."""

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        """Advance node to checkpoint. Returns True if checkpoint reached."""
        return False

    def execute(self: Self, delta: float) -> bool:
        """
        Execute the behavior of the node.

        Returns True if the node has completed its task
        and the sequencer should continue to the next node.
        """
        if self.func:
            self.func()
        return True

    def render(self: Self) -> None:
        """Render code for the current node (can apply to the GL canvas or the imgui window)."""

    # Should be overloaded
    def __repr__(self: Self) -> str:
        return self.name


class SeqCheckpoint(SeqBase):
    """Checkpoint node. Used to jump to a specific point in the TAS route."""

    def __init__(self: Self, checkpoint_name: str, return_path: SeqBase = None) -> None:
        super().__init__(
            name=checkpoint_name,
        )
        self.return_path = return_path
        self.skipped_to = False

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        blackboard().log_checkpoint(f"{self.name} (skipped)")
        self.skipped_to = checkpoint == self.name
        return self.skipped_to

    def execute(self: Self, delta: float) -> bool:
        done = True
        # Optionally, run a return to route sequence, for when the save point is out of the way
        if self.skipped_to and self.return_path is not None:
            done = self.return_path.execute(delta)
        if done:
            blackboard().log_checkpoint(self.name)
        return done


class SeqList(SeqBase):
    """A list of other nodes. Can be used to create a hierarchical tree."""

    def __init__(
        self: Self,
        name: str,
        children: list[SeqBase],
        func: Callable = None,
        shadow: str = False,
    ) -> None:
        self.step = 0
        self.children = children
        self.shadow = shadow
        super().__init__(name, func=func)

    def reset(self: Self) -> None:
        self.step = 0
        return super().reset()

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        num_children = len(self.children)
        while self.step < num_children:
            cur_child = self.children[self.step]
            if cur_child.advance_to_checkpoint(checkpoint):
                return True
            self.step += 1
        return False

    # Return true if the sequence is done with, or False if we should remain in this state
    def execute(self: Self, delta: float) -> bool:
        super().execute(delta)
        num_children = len(self.children)
        if self.step >= num_children:
            return True
        cur_child = self.children[self.step]
        # Perform logic of current child step
        ret = cur_child.execute(delta=delta)
        if ret is True:  # If current child is done
            self.step = self.step + 1
        return False

    def render(self: Self) -> None:
        num_children = len(self.children)
        if self.step >= num_children:
            return
        cur_child = self.children[self.step]
        cur_child.render()

    def __repr__(self: Self) -> str:
        num_children = len(self.children)
        if self.step >= num_children:
            return f"{self.name}[{num_children}/{num_children}]"
        cur_child = self.children[self.step]
        if self.shadow:
            return f"{cur_child}"
        cur_step = self.step + 1
        return f"{self.name}[{cur_step}/{num_children}] =>\n  {cur_child}"


class SeqIf(SeqBase):
    """
    Node to implement an if statement.

    Can be used to create conditional branching execution of the TAS route.

    To use this node, create a new class that inherits from it and override
    the `condition` method to implement the specific behavior.

    During runtime, if the `condition` method evaluates to True, the
    `when_true` node will be executed, else the `when_false` node will be executed.

    When iterating over the tree to advance to a checkpoint, the `default` branch
    will be used.
    """

    def __init__(
        self: Self,
        name: str,
        when_true: SeqBase,
        when_false: SeqBase,
        default: bool = False,
    ) -> None:
        super().__init__(name)
        self.when_true = when_true
        self.when_false = when_false
        self.default = default
        self.selection = None

    def reset(self: Self) -> None:
        self.selection = None

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        branch = self.when_true if self.default else self.when_false
        if branch:
            return branch.advance_to_checkpoint(checkpoint)
        return False

    # OVERRIDE
    def condition(self: Self) -> bool:
        """Override to implement if statement."""
        return self.default

    def execute(self: Self, delta: float) -> bool:
        if self.selection is None:
            self.selection = self.condition()
        branch = self.when_true if self.selection else self.when_false
        return branch.execute(delta) if branch is not None else True

    def render(self: Self) -> None:
        if self.selection is None:
            return
        branch = self.when_true if self.selection else self.when_false
        if branch is not None:
            branch.render()

    def __repr__(self: Self) -> str:
        if self.selection is None:
            return self.name
        branch = self.when_true if self.selection else self.when_false
        if branch is not None:
            return f"{self.name}({self.selection}): {branch.__repr__()}"
        return f"{self.name}({self.selection}): Null"


class SeqWhile(SeqBase):
    """
    Iterate over a child node over and over until the `condition` method returns False.

    To use this node, create a class and inherit from `SeqWhile`,
    then override the `condition` method.
    """

    def __init__(self: Self, name: str, child: SeqBase, default: bool = False) -> None:
        super().__init__(name)
        self.child = child
        self.default = default
        self.result = None

    def reset(self: Self) -> None:
        self.result = None

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        return self.child.advance_to_checkpoint(checkpoint) if self.default else False

    # OVERRIDE
    def condition(self: Self) -> bool:
        """Override to implement while statement."""
        return self.default

    def execute(self: Self, delta: float) -> bool:
        # First time
        if self.result is None:
            self.result = self.condition()
        # Check loop condition
        if self.result is True:
            ret = self.child.execute(delta)
            # Loop is done, recalculate loop condition
            if ret is True:
                self.result = self.condition()
        # If result is False, we are done
        return not self.result

    def render(self: Self) -> None:
        if self.result is None:
            return
        self.child.render()

    def __repr__(self: Self) -> str:
        if self.result is None:
            return self.name
        return f"While({self.name}): {self.child.__repr__()}"


class SeqBlackboard(SeqBase):
    """Set an attribute in the blackboard. Can be used for progress markers."""

    def __init__(self: Self, name: str, key: str, value: Any) -> None:  # noqa: ANN401
        super().__init__(name)
        self.key = key
        self.value = value

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        blackboard().set_dict(self.key, self.value)
        return False

    def execute(self: Self, delta: float) -> bool:
        blackboard().set_dict(self.key, self.value)
        return True
