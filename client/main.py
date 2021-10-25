from asyncio import run
from program import Program
from update import Update
from update import subscriptions
from model import initialise_model as init
if __name__ == '__main__':
    program = Program(init, Update, subscriptions)
    run(program.start())
