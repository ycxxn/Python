import math

class Circle:
    def __init__(self,radius=1):
        self.__radius=radius
    
    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2*self.__radius*math.pi

    def getArea(self):
        return self.__radius*self.__radius*math.pi

def main():
    c=Circle(5)
    print(c.getRadius())

if __name__ == "__main__":
    main()
