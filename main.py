import asyncio
from datetime import datetime
from typing import *
from enum import Enum, auto

async def listen(): ...


async def process(): ...


async def send(): ...


def failure(): ...


class Msg(Enum):
    Listen = auto()
    Process = auto()
    Send = auto()
    Failure = auto()


class Model:
    def __init__(self):
        self.file: str = ''
        self.available: bool = True

    def __set__(self, instance, value):
        if self.available:
            self.file = value
            self.available = False


init = lambda: (Model, Msg.Listen)


async def update(model: Model, msg: Msg) -> (Model, Msg):
    match msg:
        case Msg.Listen:
            print(f'listen {model} {msg}')
        case Msg.Proccesed:
            print(f'received {model} {msg}')
            return (Model.Process(), Msg.Processed)
        case Msg.Nothing:
            print(f'Nothing {model} {msg}')
            return (Model.Listen, Msg.Nothing)
        case _:
            return (Model.Listen, Msg.Nothing)


async def subscriptions(): ...


class Program:

    def __init__(self, initial_data, update, subscriptions):
        self.init = initial_data()
        self.update = update
        self.subscriptions = subscriptions

    async def __call__(self, *args, **kwargs):
        model, msg = self.init
        await self.update(model, msg)


if __name__ == '__main__':
    start = datetime.now()
    with Program(init, update, subscriptions) as program:
        asyncio.run(program())
    done = datetime.now()
    print(f'ran {start} {done} ({start - done}')

