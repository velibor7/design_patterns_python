class FlyBehaviorInterface():
    def fly(self):
        #! interface method
        pass


class NoFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("No Flying")


class SimpleFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("Simple Flying")


class JetFlying(FlyBehaviorInterface):
    @staticmethod
    def fly():
        print("Jet Flying")
