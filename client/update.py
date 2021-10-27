from client.model import Msg
from contextlib import asynccontextmanager, AsyncContextDecorator
from asyncio import run


class AsyncContextManager(AsyncContextDecorator):
    async def __aenter__(self):
        print('starting')
        return self

    async def __aexit__(self, *exc):
        print('Finishing')
        return False


class Update:
    """
    responsible for updating the state
    The arguments are Model and Msg, according to the Msg it calls
    the appropriate action to perform and return the updated Model.
    """

    def __init__(self, model, msg):
        self._model = model
        self._msg = msg

    async def update(self, msg: Msg):
        match msg:
            case Msg.Listen:
                print('listen')
                async with self.listen() as listen:
                    print(f'with {listen}')
                self.update(Msg.Process)
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

    @AsyncContextManager
    async def listen(self):
        print('listen function')
        # Update.update(model, Msg.Process)

    @AsyncContextManager
    async def process(self):
        ...

    @AsyncContextManager
    async def send(self):
        ...

    @AsyncContextManager
    def failure(self):
        ...


async def subscriptions(): ...
