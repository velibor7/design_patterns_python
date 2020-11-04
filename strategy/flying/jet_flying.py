from .fly_behavior import FlyBehaviorInterface


class JetFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("Jet Flying")