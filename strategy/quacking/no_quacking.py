from .quack_behavior import QuackBehaviorInterface


class NoQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("No Quacking")
