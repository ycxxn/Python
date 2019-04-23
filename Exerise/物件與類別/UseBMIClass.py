from BMI import BMI

def main():
    bmi1=BMI("Kevin",23,66,170)
    print("The BMI for",bmi1.getName(),"is",bmi1.getBMI(),bmi1.getStatus())

if __name__ == "__main__":
    main()