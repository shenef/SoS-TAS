import logging
from datetime import datetime
from typing import Any

logger = logging.getLogger("Timekeeping")

_TIME_FORMAT = "%H:%M:%S"


def timestr(time: datetime) -> str:
    return f"{time.strftime(_TIME_FORMAT)}.{int(time.strftime('%f')) // 1000:03d}"


class Checkpoint:
    def __init__(self, name: str, timestamp: datetime, duration: datetime) -> None:
        self.name = name
        self.timestamp = timestamp
        self.duration = duration

    def __repr__(self) -> str:
        return (
            f"Checkpoint at [{timestr(self.timestamp)}] {self.name} "
            + f"(Duration: {timestr(self.duration)})"
        )


class Blackboard:
    def __init__(self) -> None:
        self.start_time = datetime.now()
        self.last_timestamp = self.start_time
        self.checkpoints: list[Checkpoint] = []
        self.dict: dict[str, Any] = {}

    # Dictionary
    def get(self, key: str, default: Any = None) -> Any | None:
        return self.dict.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.dict[key] = value

    # Time related functions
    def start(self):
        self.start_time = datetime.now()
        self.last_timestamp = self.start_time
        logger.info("Starting timer")

    def log_checkpoint(self, name: str):
        now = datetime.now()
        duration = datetime.utcfromtimestamp(
            (now - self.last_timestamp).total_seconds()
        )
        timestamp = datetime.utcfromtimestamp((now - self.start_time).total_seconds())
        self.last_timestamp = now

        checkpoint = Checkpoint(name=name, timestamp=timestamp, duration=duration)
        self.checkpoints.append(checkpoint)
        logger.info(checkpoint)

    def stop(self):
        logger.info("Sections:")
        for checkpoint in self.checkpoints:
            logger.info(f"  {checkpoint}")

        checkpoint = self.checkpoints[-1]
        logger.info(f"Final time: {timestr(checkpoint.timestamp)}")


_blackboard = Blackboard()


def clear_blackboard():
    global _blackboard
    _blackboard = Blackboard()


def blackboard() -> Blackboard:
    global _blackboard  # noqa: PLW0602
    return _blackboard
