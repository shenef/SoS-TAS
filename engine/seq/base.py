# Libraries and Core Files
import logging
from collections.abc import Callable
from typing import Self

from engine.blackboard import blackboard

logger = logging.getLogger(__name__)


class SeqBase:
    def __init__(self: Self, name: str = "", func: Callable = None) -> None:
        self.name = name
        self.func = func

    def reset(self: Self) -> None:
        pass

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        return False

    # Return true if the sequence is done with, or False if we should remain in this state
    def execute(self: Self, delta: float) -> bool:
        if self.func:
            self.func()
        return True

    def render(self: Self) -> None:
        pass

    # Should be overloaded
    def __repr__(self: Self) -> str:
        return self.name


class SeqCheckpoint(SeqBase):
    def __init__(self: Self, checkpoint_name: str) -> None:
        super().__init__(
            name="Checkpoint",
        )
        self.checkpoint = checkpoint_name

    def advance_to_checkpoint(self: Self, checkpoint: str) -> bool:
        blackboard().log_checkpoint(f"{self.checkpoint} (skipped)")
        return checkpoint == self.checkpoint

    def execute(self: Self, delta: float) -> bool:
        blackboard().log_checkpoint(self.checkpoint)
        return True


class SeqList(SeqBase):
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
        # Peform logic of current child step
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
