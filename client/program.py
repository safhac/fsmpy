
class Program:

    def __init__(self, initial_data, update, subscriptions):
        self.init = initial_data()
        self.update = update
        self.subscriptions = subscriptions


