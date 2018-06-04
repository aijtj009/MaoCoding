import random 
f=open("95X7=.doc","w")
i=0
while i<800:
    j=random.randint(11,99)
    k=random.randint(2,9)
    n=j*k
    if j % 10 == 0: continue
    f.write(str(j)+"X"+str(k)+"="+" "*5)
    i+=1
    if i%9==0: f.write("\n")
f.close()
print("95X7=.doc Generated.")