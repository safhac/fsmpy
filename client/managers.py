import os
import asyncio
from contextlib import AbstractContextManager, AbstractAsyncContextManager
from model import Msg, TaskFailure
from model import PORT
from model import HOST
from model import TaskResult


async def listen(self):
    try:
        reader, writer = await asyncio.open_connection(
            HOST, PORT)

    except ConnectionRefusedError as e:
        print('connection error')
        # log error
        print(e.args)
        return None, e.args[1]

    else:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

    finally:
        print('listen complete')


async def process():
    ...


async def send():
    ...


async def failure():
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
            print(os.environ['PORT'])
            self.port = os.environ['PORT']

        except KeyError:
            # log error
            print('cant find port')
            self.port = PORT

    async def __aenter__(self):
        print(f'aenter listen')
        result = self.action(self)
        print(f'enter {result} {type(result)}')
        return result
        print('listen complete')

    async def __aexit__(self, *exc):

        print(f'aexit listen {exc=}')
        if not exc or ConnectionRefusedError in exc:
            print('in')
            return TaskFailure('ConnectionRefusedError', True)
        return TaskFailure('Unknown error', False)

    def run(self, *args, **kwargs):
        return self.action()

    # def action(self):
    #     return self.action()
