from client.model import Msg
from contextlib import asynccontextmanager, AsyncContextDecorator, ContextDecorator
import asyncio


class mycontext(ContextDecorator):
    def __init__(self, *args, **kwargs):
        ...
    def __enter__(self):
        print('starting')
        print(type(self))
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False


@mycontext
def listen(*args):
    print('listen function')
    # Update.update(model, Msg.Process)


@mycontext
async def process():
    ...


@mycontext
async def send():
    ...


@mycontext
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

    async def start(self):
        await self.update(Msg.Listen)

    async def update(self, msg: Msg):
        match msg:
            case Msg.Listen:
                print('listen')
                with listen():
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
                print('_')


async def subscriptions(): ...
