from abc import ABC, abstractmethod

class Country(ABC):
    @abstractmethod
    def continent(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Georgia(Country):
    def continent(self):
        print("Country is in Europe")

    def name(self):
        print("Name of the country is Georgia")

    def area(self):
        print("Area is 69,700 km2")

    def __init__(self):
        self._budget = "Budget is 23 Billion"
        self.population = "Population is 3.7 Million"
        self.__politics = "Error"


georgia = Georgia()
georgia.continent()
georgia.name()
georgia.area()

print(georgia._budget)
print(georgia.population)
# print(georgia.__politics)