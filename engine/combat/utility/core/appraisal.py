import logging
from typing import Self

logger = logging.getLogger(__name__)


class Appraisal:
    def __init__(self: Self, value: int = 0) -> None:
        self.value: int = value
        self.target: str = None
        self.complete: bool = False

    def execute(self: Self) -> None:
        logger.debug("No appraiser execution defined.")
        logger.debug("Please ensure your Appraisal implements the execute() function")
