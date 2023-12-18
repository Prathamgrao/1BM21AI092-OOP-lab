from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def milage(self):
        pass
    def wheels(self):
        print("4 wheels")
class tata(car):
    def milage(self):
        print("tata milage is 35")
class maruthi(car):
    def milage(self):
        print("maruthi milage is 31")
class ford(car):
    def milage(self):
        print("ford milage is 21")
t=tata()
m=maruthi()
f=ford()
t.milage()
m.milage()
f.milage()
f.wheels()
