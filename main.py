import asyncio
from datetime import datetime
from typing import *

"""
MODEL : state
Update: a function that updates the model
it's arguments are the old model, a command with arguments
Cmd: the event that occured 
Msg: are the arguments for command


"""

class Update:
    pass

class Main:
    pass

class Model:
    pass

class View:
    pass


class Program:
    def __init__(self, main, *args, **kwargs):
        self.__main__ = main
        loop = asyncio.
    async def __call__(self, *args, **kwargs):
        await self.__main__()


received = TypeVar("received")
process = TypeVar("process")
send = TypeVar("send")

Command = received | process | send


class Command:
    pass


def immutable(args):
    pass


@immutable


Model = lambda: {
    'file': None
}


class File:
    input_date: datetime
    process_time: int


class Cmd:


def update(model: Model, cmd: Cmd):
    match cmd:
        case received:
            ...
        case process:
            ...
        case send:
            ...
        case sent:
            ...


async def socket_listener():

async def main():
    pass

if __name__ == '__main__':
    loop = asyncio.get_running_loop()
    loop.run_until_complete(main())
