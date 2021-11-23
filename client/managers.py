import os
import asyncio
from contextlib import AbstractContextManager, AbstractAsyncContextManager
from model import Msg, TaskFailure
from model import PORT
from model import HOST
from model import TaskResult


async def listen(event):
    """await incoming data"""
    # avail_port = os.environ.get('PORT', PORT)
    avail_port = PORT
    try:
        print('listening')
        reader, writer = await asyncio.open_connection(
            HOST, avail_port)

    except ConnectionRefusedError as e:
        print('ConnectionRefusedError', e.args)
        result = TaskFailure('ConnectionRefusedError', True)

    except BaseException as e:
        print(f'other exception {e.args}')
        raise

    else:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")
        result = TaskResult(data, True)

    finally:
        print('listen complete')
        return result


async def process():
    """process the data"""
    ...


async def send():
    """send the processed data"""
    ...


async def failure():
    """log fail events"""
    ...


action_map = dict(
    zip(
        list(Msg.__members__)[:-1],
        [listen, process, send, failure]
    ))


class ActionManager(AbstractAsyncContextManager):

    def __init__(self, context: Msg):

        self.host = HOST
        self.action = action_map[context.name]

        try:
            self.port = os.environ['PORT']

        except KeyError:
            # log error
            print('cant find port')
            self.port = PORT

    async def __aenter__(self):
        await self.action(self)
        print('context complete')

    async def __aexit__(self, *exc):
        print(f'aexit context {exc=}')
        if ConnectionRefusedError in exc:
            return TaskFailure('ConnectionRefusedError', True)
        return TaskFailure('Unknown error', False)
