import asyncio
from contextlib import ContextDecorator

from model import HOST, PORT


class Listen(ContextDecorator):

    def __enter__(self):

        print(f'enter listen')
        # data = reader.read(100)
        # message = data.decode()

        # print(f"Received {message!r}")
        print('listen complete')
        # return message

        print(f'exit listen')

    def __exit__(self, *exc):
        # self._reader.close()

        print(f'exit listen {exc=}')
