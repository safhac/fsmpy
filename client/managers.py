import os
import asyncio
from contextlib import AbstractAsyncContextManager
from model import Msg, TaskResult
from model import PORT
from model import HOST
from model import TaskResult


def named(name: str, suppress_list: set = None):
    """function __name__ property decorator"""

    def inner(func: object):
        func.__name__ = name
        func.__suppress_list__ = suppress_list
        return func

    return inner


@named('listen', {ConnectionRefusedError})
async def listen(event: asyncio.Event) -> TaskResult:
    """await incoming data"""
    print(f'listen function {event}')
    event.set()
    avail_port = os.environ.get('PORT', PORT)
    # avail_port = PORT
    try:
        reader, writer = await asyncio.open_connection(
            HOST, avail_port)

    except ConnectionRefusedError as e:
        print('ConnectionRefusedError', e.args)
        result = TaskResult(e.args, False)
    except BaseException as e:
        print(f'other exception {e.args}')
        raise

    else:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")
        return TaskResult(data, True)

    finally:
        print('listen complete')
        return result



@named('send')
async def send():
    """send the processed data"""
    ...


@named('process')
async def process():
    """process the data"""
    ...


@named('failure')
async def failure():
    """log fail events"""
    ...


action_map = dict(
    zip(
        list(Msg.__members__)[:-1],
        [listen, process, send, failure]
    ))


class Awaitable(AbstractAsyncContextManager):
    def __init__(self, action, event=asyncio.Event()):
        self.event = event
        self.action = action
        print(f'awaitable {action} {self.event}')
        self.awaitable = asyncio.create_task(
            action(self.event),
            name=action.__name__
        )

    async def __aenter__(self):
        return await self.awaitable

    async def __aexit__(self, *exc):
        print(f'aexit context {exc=}')

        if exc[0] in self.action.__suppress_list__:
            print('suppressed')
            return TaskResult(exc[0], True)
        return TaskResult('Unknown error', False)
