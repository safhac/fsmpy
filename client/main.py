import asyncio
from program import Program
from model import Model
from model import Msg
from update import Update
from update import subscriptions

init = lambda: (Model, Msg.Listen)

if __name__ == '__main__':
    program = Program(init, Update, subscriptions)
    asyncio.run(program.run())
