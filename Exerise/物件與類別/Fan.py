class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color="blue"):
        self.__speed = speed
        self.on = False
        self.radius = radius
        self.__color = color

    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False

    def getSpeed(self):
        return self.__speed

    def getOn(self):
        return self.on

    def getColor(self):
        return self.__color

    def getRadius(self):
        return self.radius
    

    
    
    
