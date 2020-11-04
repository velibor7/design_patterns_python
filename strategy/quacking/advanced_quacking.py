from .quack_behavior import QuackBehaviorInterface


class AdvancedQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("Advanced Quacking")
