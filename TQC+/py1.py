def main():
    sum=0
    Number_=5
    numbers=[]
    for i in range(Number_):
        value=float(input("請輸入四個數字:"))
        numbers.append(value)
        sum+=value
    
    print("平均值=",sum/4)
    numbers[0]= '%5.2f' % numbers[0]
    numbers[1]= '%5.2f' % numbers[1]
    numbers[2]= '%5.2f' % numbers[2]
    numbers[3]= '%5.2f' % numbers[3]
    numbers[4]= '%5.2f' % numbers[4]
    print("=======")
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    print(numbers[3])
    print(numbers[4])
    print("=======")


if __name__=='__main__':
    main()
    
    