from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class Msg(Enum):
    Listen = auto()
    Process = auto()
    Send = auto()
    Failure = auto()
    NoOp = auto()


@dataclass
class DataStatus:
    processed: bool = False
    received: datetime = None


@dataclass(frozen=True)
class Model:
    state: DataStatus
    data: str = None


def init() -> (Model, Msg):
    return Model(), Msg.Listen
