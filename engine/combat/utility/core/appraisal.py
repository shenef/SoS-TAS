import logging
from typing import Self

logger = logging.getLogger(__name__)


class Appraisal:
    def __init__(self: Self, name: str, value: float = 0) -> None:
        self.name: str = name
        self.value: float = value
        self.target: str = None
        self.complete: bool = False

    def execute(self: Self) -> None:
        logger.debug("No appraiser execution defined.")
        logger.debug("Please ensure your Appraisal implements the execute() function")

    def __repr__(self: Self) -> str:
        return self.name
