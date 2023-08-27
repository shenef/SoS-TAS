import logging

logger = logging.getLogger(__name__)


class Appraisal:
    def __init__(self):
        self.value = 0

    def execute(self):
        logger.debug("No appraiser execution defined.")
        logger.debug("Please ensure your Appraisal implements the execute() function")
