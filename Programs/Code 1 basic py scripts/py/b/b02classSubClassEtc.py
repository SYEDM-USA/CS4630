class Vehicle:
 
    def __init__(self, name, color):
        self.__name = name      # __name is private to Vehicle class
        self.__color = color
    def getName(self):     
        return self.__name
    def getColor(self):   
        return self.__color
    def setColor(self, color):
        self.__color = color
 
class Car(Vehicle): #Car is a subclass of Vehicle
 
    def __init__(self, name, color, model):
        super().__init__(name, color) # base const called     
        self.__model = model
 
    def getDescription(self):
        return self.getName() + self.__model \
        + " in " + self.getColor() 
