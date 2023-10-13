import logging
from typing import Self

logger = logging.getLogger(__name__)


class Appraisal:
    def __init__(self: Self, value: int = 0) -> None:
        self.value = value
        self.target = None
        self.complete = False

    def execute(self: Self) -> None:
        logger.debug("No appraiser execution defined.")
        logger.debug("Please ensure your Appraisal implements the execute() function")
