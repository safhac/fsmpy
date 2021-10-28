from update import Update
from model import Model
from model import Msg
import asyncio


class Program:
    """
    The class represents the program primary parts
    Initial state, Update method, Subscription method
    The program is initiated with init initial state,
    the update function and the subscriptions
    event listener function.
    """

    def __init__(self, init: (Model, Msg), update: Update, subscriptions):
        model, msg = init()
        self.update = update(model, msg)
        self.subscriptions = subscriptions

    def run(self):
        asyncio.run(self.update.update())
