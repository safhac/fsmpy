import asyncio

from client.model import Model, TaskResult, TaskFailure
from client.model import new_model
from client.model import Msg

from managers import ActionManager
from managers import listen


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
                # update model
                self._model = new_model()
                event = asyncio.Event()
                listen_task = asyncio.create_task(listen(event))
                event.set()
                await listen_task

            case Msg.Process:

                print('process')
                print(self._model)
            case Msg.Send:
                print('send')
            case Msg.Failure:
                print('failure')
                print(self._model)
            case Msg.NoOp:
                print('noop')
            case _:
                print(f'msg is {msg}')


async def subscriptions(): ...
