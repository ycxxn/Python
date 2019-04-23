class BMI:
    def __init__(self,name,age,weight,height):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height

    def getBMI(self):
        #KILOGRAMS_PER_POUND = 0.45359237
        #METERS_PER_INCH = 0.0254
        bmi = self.__weight/(self.__height*self.__height/10000)
        return bmi
    
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "過輕"
        if 18.5 <= bmi < 24:
            return "正常"
        if bmi >= 24:
            return "過重"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getHeight(self):
        return self.__height

    def getWeight(self):
        return self.__weight 
