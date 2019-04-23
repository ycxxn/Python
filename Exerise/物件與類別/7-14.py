class A:
    def __init__(self,newS="Welcome"):
        self.__s=newS

    def print(self):
        print(self.__s)

def main():
    a=A()
    a.print()

if __name__ == "__main__":
    main()