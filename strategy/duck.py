class Duck():
    def __init__(self, flybeh, quackbeh):
        self.fly_behavior = flybeh
        self.quack_behavior = quackbeh

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()