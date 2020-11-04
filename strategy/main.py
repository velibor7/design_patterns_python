from duck import Duck
from quack_behavior import SimpleQuacking, AdvancedQuacking, NoQuacking
from fly_behavior import SimpleFlying, JetFlying, NoFlying

if __name__ == "__main__":
    wild_duck = Duck(SimpleFlying, AdvancedQuacking)
    city_duck = Duck(JetFlying, SimpleQuacking)
    rubber_duck = Duck(NoFlying, NoQuacking)

    wild_duck.fly()
    city_duck.fly()
    rubber_duck.fly()
    wild_duck.quack()
    city_duck.quack()
    rubber_duck.quack()