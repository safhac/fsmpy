import time
import asyncio
from client.model import Msg, PORT, HOST

from managers import Listen


async def listen():
    try:
        reader, writer = await asyncio.open_connection(
            HOST, PORT)
    except ConnectionRefusedError as e:
        print(e.args[0])
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
                with Listen():
                    await listen()
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
