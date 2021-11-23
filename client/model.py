from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
from typing import TypeVar
from typing import Protocol

T = TypeVar("T")

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


@dataclass(frozen=True)
class Model:
    state: DataState
    data: str = None


def initialise_model() -> (Model, Msg):
    initial_data_status = DataState()
    return Model(initial_data_status, None), Msg.Listen


@dataclass
class TaskResult:
    result: T
    success: bool


@dataclass
class TaskFailure:
    result: T
    success: bool


new_model = lambda: Model(new_state())
new_state = lambda: DataState(False, datetime.now())
