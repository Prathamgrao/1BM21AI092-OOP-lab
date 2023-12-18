class vehicle:
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
    @abstractmethod
    def start(self):
        pass
class bike(vehicle):
    no_of_wheels=2
    def display(self):
        print("kick_start")
class car(vehicle):
    no_of_wheels=4
    def display(self):
        print("selfstart")
class bus(vehicle):
    no_of_wheels=6
    def display(self):
        print("leverstart")
        
b1=bike(2)
b1.display() 
c1=car(4)
c1.display()
bus1=bus(6)
bus1.display()
