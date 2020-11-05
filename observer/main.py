from weather_station import WeatherStation, ObservableInterface
from displays import PhoneDisplay, WindowDisplay

if __name__ == "__main__":
    weather_station = WeatherStation()

    my_phone = PhoneDisplay(weather_station)
    sljivas_phone = PhoneDisplay(weather_station)

    my_window = WindowDisplay(weather_station)
    sljivas_window = WindowDisplay(weather_station)

    print(f"Temperature before update is: {my_phone.temperature}")

    weather_station.add(my_phone)
    weather_station.add(sljivas_phone)
    weather_station.add(my_window)
    weather_station.add(sljivas_window)

    weather_station.notify()

    print(f"Temperature after update is: {my_phone.temperature}")
