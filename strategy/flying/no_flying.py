from .fly_behavior import FlyBehaviorInterface


class NoFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("No Flying")