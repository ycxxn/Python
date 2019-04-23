class Fan2:
    
    def __init__(self):
        self.SLOW = 1
        self.MEDIUM = 2
        self.FAST = 3
        self.__speed = self.SLOW
        self.__on = False
        self.__radius = 5
        self.__color = "blue"

    def getSpeed(self):
        return self.__speed
    
    def getOn(self):
        return self.__on
    
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color
    
    def turnOn(self):
        self.__on = True
    
    def turnOff(self):
        self.__on = False
    
    def setSpeed(self,speed):
        self.__speed = speed
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def setColor(self,color):
        self.__color = color
    

def main():
    fan1 = Fan2()
    print(fan1.getSpeed(),fan1.getOn(),fan1.getRadius(),fan1.getColor())

    fan2 = Fan2()
    fan2.setSpeed(fan2.FAST)
    fan2.turnOn()
    fan2.setRadius(10)
    fan2.setColor("yellow")
    print(fan2.getSpeed(),fan2.getOn(),fan2.getRadius(),fan2.getColor())

    fan3 = Fan2()
    print(fan3.getSpeed(),fan3.getOn(),fan3.getRadius(),fan3.getColor())

if __name__ == "__main__":
    main()