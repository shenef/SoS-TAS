from typing import Self


class ReasonerExecutionContext:
    """Handles configurable parameters for the reasoner."""

    def __init__(self: Self, priority_targets: list[str] = None) -> None:
        """Initialize a new ReasonerExecutionContext object."""
        if priority_targets is None:
            priority_targets = []
        self.priority_targets: list[str] = priority_targets
