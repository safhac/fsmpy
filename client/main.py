import asyncio
from datetime import datetime
from app_program import Program
from app_model import Model
from app_types import Msg
from app_update import update, subscriptions

init = lambda: (Model, Msg.Listen)

if __name__ == '__main__':
    program = Program(init, update, subscriptions)
    asyncio.run(program())
