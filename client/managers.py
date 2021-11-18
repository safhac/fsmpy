import os
import asyncio
from contextlib import AbstractContextManager
from model import Msg
from model import PORT
from model import HOST


async def listen(self):
    try:
        reader, writer = await asyncio.open_connection(
            HOST, PORT)

    except ConnectionRefusedError as e:
        print('connection error')
        # log error
        print(e.args)
        return (None, e.args[1])

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


class ActionManager(AbstractContextManager):

    def __init__(self, context: Msg):

        self.host = HOST

        try:
            self.port = os.environ['PORT']

        except KeyError:
            # log error
            print('cant find port')
            self.port = PORT

    def __enter__(self):
        print(f'enter listen')
        return (self, None)
        print('listen complete')

    def __exit__(self, *exc):

        print(f'exit listen {exc=}')
        if not exc or ConnectionRefusedError in exc:
            print('in')
            return True
        return False

    def run(self, *args, **kwargs):
        return self.action()

    # def action(self):
    #     return self.action()
