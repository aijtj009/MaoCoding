import math
n=20000
primes=[2]
for i in range(3,n+1,2):
    Prime=True
    for j in range(3,int(math.sqrt(i))+2,2):
        if i%j==0:
            Prime=False
            break
    if Prime:
        primes.append(i)
print(primes)
for i in range(3,n+1):
    divide=[]
    m=i
    for j in primes:
        if j>int(math.sqrt(m))+2:
            break
        while m%j==0:
            m=m//j
            CanDivide=True
            divide.append(j)
    if m!=1:
        divide.append(m)
    printString=str(i)+'='
    if len(divide)>1:
        for k in divide:
            printString=printString+str(k)+'X'
    print(printString[0:-1],end='  ')