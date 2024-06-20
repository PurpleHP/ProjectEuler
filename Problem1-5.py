from numpy import square


def problem1():
    sumOfNum = 0
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            sumOfNum+=i
    print(sumOfNum)

def problem2():
    arr = [1,1,2]
    sumOfNum, i = 2, 3
    while(True):
        arr[i%3] = arr[(i+2)%3] + arr[(i+1)%3]
        if arr[i%3] > 4000000:
            break
        if (arr[i%3] % 2) ==0:
            print(arr[i%3])
            sumOfNum += arr[i%3]
        i += 1
    print(sumOfNum)

def problem3():
    def isPrime(a):
        for i in range(2,int(a/2)):
            if a % i == 0:
                return False
        return True
    i = 1
    num = 600851475143
    while num > 1:
        i+=2
        if isPrime(i) and (num%i ==0):
            num = num/i     
    print(i)

    
