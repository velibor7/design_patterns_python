class ObserverInterface:
    def update(self):
        pass

    def display(self):
        pass


class PhoneDisplay(ObserverInterface):
    def __init__(self, weather_station):
        self.weather_station = weather_station
        self.temperature = 0

    # update is called when weather station wants to update
    def update(self):
        self.temperature = self.weather_station.get_temperature()

    def display(self):
        print(f"(Phone) Temperature is {self.temperature}")


class WindowDisplay(ObserverInterface):
    def __init__(self, weather_station):
        self.weather_station = weather_station
        self.temperature = 0

    # update is called when weather station wants to update
    def update(self):
        self.temperature = self.weather_station.get_temperature()

    def display(self):
        print(f"(Window) Temperature is {self.temperature}")