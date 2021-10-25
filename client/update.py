from model import Msg
from contextlib import asynccontextmanager

class Update:
    """
    responsible for updating the state
    The arguments are Model and Msg, according to the Msg it calls
    the appropriate action to perform and return the updated Model.
    """
    def __init__(self, model, msg):
        self._model = model
        self._msg = msg

    @asynccontextmanager
    async def update(self, *args, **kwargs):
        self._msg = yield
        match self._msg:
            case Msg.Listen:
                print('listen')
                await listen(self._model)
            case Msg.Process:
                print('process')
                await listen(self._model)
            case Msg.Send:
                print('send')
                await listen(self._model)
            case Msg.Failure:
                print('failure')
                await listen(self._model)
            case Msg.NoOp:
                print('noop')
                await listen(self._model)
            case _:
                print('_')
                await listen(self._model)


async def listen(model):
    print('listen function')
    Update(model, Msg.Process)


async def process(): ...


async def send(): ...


def failure(): ...


async def subscriptions(): ...
