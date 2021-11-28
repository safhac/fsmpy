from client.model import new_model
from client.model import Msg
from client.model import TaskResult

from client.managers import Awaitable
from client.managers import listen
from client.managers import process


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

                async with Awaitable(listen) as action:
                    print(f'with {action}')
                    task = await action
                    self._model.data = task.result

                    await self.update(Msg.Process) if task.success else self.update(Msg.Failure)
                print('out of with')
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
