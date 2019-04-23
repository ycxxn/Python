class Car:
    def __init__(self, wheels_number, car_doors, passengers):
        self.wheels_number = wheels_number
        self.car_doors = car_doors
        self.passengers = passengers

class SUV(Car):
    def __init__(self,wheels_number,car_doors,passengers,name,air_bags):
        super().__init__(wheels_number,car_doors,passengers)
        self.name=name
        self.air_bags=air_bags

    def getDetail(self):
        print(wheels_number)
        print(car_doors)
        print(passengers)
        print(name)
        print(air_bags)
    
class Super_Car(Car):
    def __init__(self,wheels_number,car_doors,passengers,name,highspeed):
        super().__init__(wheels_number,car_doors,passengers)
        self.name=name
        self.highspeed=highspeed

    def getDetail(self):
        print(self.wheels_number)
        print(self.car_doors)
        print(self.passengers)
        print(self.name)
        print(self.highspeed)

car=Super_Car(4,2,2,"Mclaren570s",380)
car.getDetail()