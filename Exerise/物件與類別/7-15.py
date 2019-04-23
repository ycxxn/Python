class A:
    def __init__(self,on):
        self.__on = not on

    def getOn(self):
        return self.__on

def main():
    a=A(False)
    print(a.getOn())

if __name__ == "__main__":
    main()
