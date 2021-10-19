import asyncio
from datetime import datetime
from typing import *
from enum import Enum, auto


class ModelEnum(Enum):
    def __new__(cls, fn, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__call__ = fn(*args, **kwargs)
        return obj


def listen(): ...


def process(): ...


def send(): ...


def failure(): ...


class Model(ModelEnum):
    Listen = (listen)
    Process = (process)
    Send = (send)
    Failure = (failure)


class Msg(Enum):
    Received = auto()
    Wait = auto()


init = lambda: (Model.Listen, Msg.Wait)


async def update(model: Model, msg: Msg):
    match msg:
        case Msg.Received:
            ...
        case Msg.Wait:
            ...
        case _:
            ...


class Program:

    def __init__(self, init, update, subscriptions):
        self.init = init,
        self.update = update
        self.subscriptions = subscriptions

    async def __call__(self, *args, **kwargs):
        await self.update(init, Msg.Wait)


if __name__ == '__main__':
    lambda: Program(init, update)()
