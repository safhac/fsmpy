from app_model import Model
from app_types import Msg


async def update(model: Model, msg: Msg) -> (Model, Msg):
    match msg:
        case Msg.Listen:
            print(f'listen {model} {msg}')
            await listen(model)
        case Msg.Process:
            print(f'process {model} {msg}')

        case Msg.Nothing:
            print(f'Nothing {model} {msg}')
            return (Model.Listen, Msg.Nothing)
        case _:
            return (Model.Listen, Msg.Nothing)


async def listen(model):
    await update(model, Msg.Process)


async def process(): ...


async def send(): ...


def failure(): ...


async def subscriptions(): ...