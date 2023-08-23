import logging

from engine.seq import SeqList, SeqLog

logger = logging.getLogger(__name__)


class DemoWorldBriskToTower(SeqList):
    def __init__(self):
        super().__init__(
            name="Brisk",
            children=[
                SeqLog(name="SYSTEM", text="TODO, move to tower!"),
                # TODO: Navigate world map, move to tower
            ],
        )
