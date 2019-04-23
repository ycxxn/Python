from Fan import Fan

def main():
    fan1=Fan(Fan.FAST,10,"yellow")
    fan1.turnOn()
    print(fan1.getSpeed(),fan1.getOn(),fan1.getRadius(),fan1.getColor())

    fan2=Fan(Fan.MEDIUM,5,"blue")
    fan2.turnOff()
    print(fan2.getSpeed(),fan2.getOn(),fan2.getRadius(),fan2.getColor())

if __name__ == "__main__":
    main()