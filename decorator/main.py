from impl import Espresso, Decaf, SoyAddOnDecorator, CaramelAddOnDecorator

if __name__ == "__main__":

    order_1 = SoyAddOnDecorator(
        CaramelAddOnDecorator(CaramelAddOnDecorator(Espresso())))

    just_espresso = Espresso()

    print(order_1.cost())
    print(just_espresso.cost())
