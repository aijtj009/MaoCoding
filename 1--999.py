"""
#1*1+3*3+.....+999*999
s=0
for i in range(1,999,2):
    s=s+i*i
print("Sum=",s)

#================
#Prime or Not?
x = 23
isPrime = True
for y in range(2,x):
    if x%y==0:
        isPrime = False
        
print (x,"is prime: ",isPrime)

"""
primeadder=0

for y in range(2,1000,2):
    w=y-1
    if y%w==1:
        primeadder+=y

print("All the prime add up in 1-1000 is:",primeadder)





