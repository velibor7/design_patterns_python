from .fly_behavior import FlyBehaviorInterface


class SimpleFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("Simple Flying")
