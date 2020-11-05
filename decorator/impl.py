from abc import ABC, abstractmethod


# component
class Beverage(ABC):
    def get_description(self):
        return "Description"

    @abstractmethod
    def cost(self):
        pass


# concrete component
class Espresso(Beverage):
    def cost(self):
        return 1.60


# concrete component
class Decaf(Beverage):
    def cost(self):
        return 1.10


# decorator
class AddOnDecorator(Beverage):
    @abstractmethod
    def cost(self):
        pass


# concrete decorator
class CaramelAddOnDecorator(AddOnDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.60


# concrete decorator
class SoyAddOnDecorator(AddOnDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 0.30
