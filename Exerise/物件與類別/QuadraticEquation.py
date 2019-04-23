import math

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def getDiscriminant(self):
        return self.__b * self.__b - (4 * self.__a * self.__c)
    
    def getRoot1(self):
        return (-self.__b + math.sqrt(self.__b * self.__b - (4 * self.__a * self.__c)))/(2*self.__a)
    
    def getRoot2(self):
        return (-self.__b - math.sqrt(self.__b * self.__b - (4 * self.__a * self.__c)))/(2*self.__a)

def main():
    x1=QuadraticEquation(1,4,3)

    if x1.getDiscriminant() > 0:
        print(x1.getRoot1(),x1.getRoot2())
    
    if x1.getDiscriminant() == 0:
        print(x1.getRoot1())

    if x1.getDiscriminant() < 0:
        print("The equation has no roots")


if __name__ == "__main__":
    main()