import math
n= 100999999
primes=[2]
for i in range(3,int(math.sqrt(n+1))+1,2):
    Prime=True
    for j in range(3,int(math.sqrt(i))+2,2):
        if i%j==0:
            Prime=False
            break
    if Prime:
        primes.append(i)
print(primes)
for i in range(2,1001):
    if i not in primes:
        print(i,end=",")

