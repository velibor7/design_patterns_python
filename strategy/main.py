from duck import Duck
from quacking import simple_quacking, advanced_quacking, no_quacking
from flying import jet_flying, no_flying, simple_flying

if __name__ == "__main__":
    wild_duck = Duck(simple_flying.SimpleFlying,
                     advanced_quacking.AdvancedQuacking)
    city_duck = Duck(jet_flying.JetFlying, simple_quacking.SimpleQuacking)
    rubber_duck = Duck(no_flying.NoFlying, no_quacking.NoQuacking)

    wild_duck.fly()
    city_duck.fly()
    rubber_duck.fly()
    wild_duck.quack()
    city_duck.quack()
    rubber_duck.quack()