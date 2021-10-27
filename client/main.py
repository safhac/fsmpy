import asyncio
from program import Program
from update import Update as update
from update import subscriptions as subs
from model import initialise_model as init



async def main(init=init, update=update, subscriptions=subs) -> None:

    program = Program(init, update, subscriptions)
    await program.run()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
