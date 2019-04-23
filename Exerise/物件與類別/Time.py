class Time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute
    
    def getSecond(self):
        return self.__second
    
    def setTime(self):
        t=[]
        for i in range(3):
            value=int(input("Enter the elaspsed time:"))
            t.append(value)
        h = t[0]
        m = t[1]
        s = t[2]
        print(self.__hour + h,":",self.__minute + m,":",self.__second + s)

def main():
    t=Time(12,41,6)
    print("Current time is",t.getHour(),":",t.getMinute(),":",t.getSecond())
    t.setTime()
    

if __name__ == "__main__":
    main()