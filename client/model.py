from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
from typing import TypeVar

T = TypeVar["T"]

PORT = 8888
HOST = '127.0.0.1'


class Msg(Enum):
    Listen = auto()
    Process = auto()
    Send = auto()
    Failure = auto()
    NoOp = auto()


@dataclass
class DataState:
    processed: bool = False
    received: datetime = None


new_state = lambda: DataState(False, datetime.now())


@dataclass(frozen=True)
class Model:
    state: DataState
    data: str = None


def initialise_model() -> (Model, Msg):
    initial_data_status = DataState()
    return Model(initial_data_status, None), Msg.Listen


new_model = lambda: Model(new_state())


@dataclass
class TaskResponse:
    success: bool
    result: T
