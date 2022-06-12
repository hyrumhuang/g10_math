#輸入數字
from unicodedata import decimal

# 計算平均值
def calcAverage(ary):
    total = 0
    for i in range(len(ary)):
        total = total + ary[i]
        # print(total)
    average = total / len(ary)
    return average 

# 計算標準差
def calcSD(ary):
    t = len(ary)
    total = 0
    average = calcAverage(ary)
    for i in range(t):
        z = ary[i] - average
        SD = (z * z)
        total = total + SD

    return (total / t) ** 0.5


# 標準化後產生新數據
def standardlize(ary):
    l = []
    t = len(ary)
    average = calcAverage(ary)
    sd = calcSD(ary)
    for i in range(t):
        z = ary[i] - average
        standardization = z / sd
        l.append(round(standardization, 1))

    return l


def relativeCoeff(ary1, ary2):
    aryNew1 = standardlize(ary1)
    aryNew2 = standardlize(ary2)
    total = 0;
    elmNum = len(aryNew1)
    for i in range(elmNum):
        total = total + ( ary1[i] * ary2[i])

    return (total / elmNum)

# 主程式
def main():
    a = []
    while(True):
        b = input("numbers: ")
        if(b == "n"):
            break
        elif(b == "w"):
            a.pop()
            print(a)
        else:
            decimal = float(b)
            a.append(round(decimal, 1))
            print(a)

    t = len(a)

    #算出平均數
    # total = 0 
    # for i in range(t):
    #     total = total + a[i]
    #     print(total)
    average = calcAverage(a)

    print("平均：" + str(average))

    #算出標準差
    standard_deviation = calcSD(a)
    print("標準差：" + str(standard_deviation))

    #算出標準化數據
    print("標準化數據")
    print(standardlize(a))

print( __name__)
if __name__ == '__main__':
    main()




