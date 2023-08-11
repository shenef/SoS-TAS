# Libraries and Core Files
import logging

from engine.seq.base import SeqBase

logger = logging.getLogger(__name__)


class SeqLog(SeqBase):
    def __init__(self, name: str, text: str):
        self.text = text
        super().__init__(name)

    def execute(self, delta: float) -> bool:
        logging.getLogger(self.name).info(self.text)
        return True


class SeqDebug(SeqBase):
    def __init__(self, name: str, text: str):
        self.text = text
        super().__init__(name)

    def execute(self, delta: float) -> bool:
        logging.getLogger(self.name).debug(self.text)
        return True
