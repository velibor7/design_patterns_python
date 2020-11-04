from .quack_behavior import QuackBehaviorInterface


class SimpleQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("Simple Quacking")
