class Program:

    def __init__(self, initial_data, update, subscriptions):
        self.init = initial_data()
        self.update = update
        self.subscriptions = subscriptions

    async def __call__(self, *args, **kwargs):
        model, msg = self.init
        await self.update(model, msg)

