import asyncio
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


@dataclass
class Model:
    state: DataState
    data: str = None


@dataclass(frozen=True)
class TaskResult:
    result: T
    success: bool


class Awaitable:
    def __init__(self, action, event=asyncio.Event()):
        self.awaitable = asyncio.create_task(
            action(event.set())
        )

    async def wait(self):
        return await self.awaitable


def initialise_model() -> (Model, Msg):
    initial_data_status = DataState()
    return Model(initial_data_status, None), Msg.Listen


new_state = lambda: DataState(False, datetime.now())
new_model = lambda: Model(new_state())
