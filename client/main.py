import asyncio
from program import Program
from update import Update as update
from update import subscriptions as subs
from model import initialise_model as init



def main(init=init, update=update, subscriptions=subs) -> None:

    program = Program(init, update, subscriptions)
    program.run()


if __name__ == '__main__':
    main()
