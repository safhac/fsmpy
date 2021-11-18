
from client.model import Model
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

                self._model = new_model()

                with ActionManager(Msg.Listen) as manager:
                    data, error = await listen(manager)

                if data:
                    self._model = Model(self._model.state, data)
                    await self.update(Msg.Process)

                elif error:
                    self._model = Model(self._model.state, error)
                    await self.update(Msg.Failure)

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
