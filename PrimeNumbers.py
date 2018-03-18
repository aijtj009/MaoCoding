import math
for i in range(111,200,2):
    Prime=True
    for j in range(3,int(math.sqrt(i))+2,2):
        if i%j==0:
            Prime=False
            break
    if Prime:
        print(i,end=' ')