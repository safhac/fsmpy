import asyncio
from datetime import datetime
from program import Program
from model import Model
from model import Msg
from update import update, subscriptions

init = lambda: (Model, Msg.Listen)

if __name__ == '__main__':
    program = Program(init, update, subscriptions)
    asyncio.run(program())
