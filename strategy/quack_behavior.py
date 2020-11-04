class QuackBehaviorInterface():
    def quack(self):
        #! interface method
        pass


#! CONCRETE IMPLEMENTATIONS
class NoQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("No Quacking")


class SimpleQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("Simple Quacking")


class AdvancedQuacking(QuackBehaviorInterface):
    @staticmethod
    def quack():
        print("Advanced Quacking")