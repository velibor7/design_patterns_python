class ObservableInterface:
    def add(self, observer):
        pass

    def remove(self, observer):
        pass

    def notify(self):
        pass


class WeatherStation(ObservableInterface):
    def __init__(self):
        self.observers = None  # collection of observers

    def add(self, observer):
        if self.observers == None or len(self.observers) == 0:
            self.observers = [observer]
        else:
            self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    # we notify each one of the observers
    def notify(self):
        for observer in self.observers:
            observer.update()

    @staticmethod
    def get_temperature():
        return 31  # dummy
