import time

from client.model import Msg
from contextlib import asynccontextmanager, AsyncContextDecorator, ContextDecorator
import asyncio


@asynccontextmanager
async def listen(*args):
    yield
    print('listen complete')
    # Update.update(model, Msg.Process)


async def process():
    ...


async def send():
    ...


async def failure():
    ...


class Update:
    """
    responsible for updating the state
    The arguments are Model and Msg, according to the Msg it calls
    the appropriate action to perform and return the updated Model.
    """

    def __init__(self, model, msg):
        self._model = model
        self._msg = msg


    async def update(self, msg=Msg.Listen):

        match msg:
            case Msg.Listen:
                print('listen')
                async with listen():
                    time.sleep(2)
                    print(f'with {listen}')
                await self.update(Msg.Process)
            case Msg.Process:
                print('process')
            case Msg.Send:
                print('send')
            case Msg.Failure:
                print('failure')
            case Msg.NoOp:
                print('noop')
            case _:
                print(f'msg is {msg}')




async def subscriptions(): ...
