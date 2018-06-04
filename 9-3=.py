import random 
f=open("9-3=.doc","w")
i=0
while i<800:
    j=random.randint(2,9)
    k=random.randint(1,8)
    n=j-k
    if n<=0: continue
    f.write(str(j)+"-"+str(k)+"="+" "*4)
    i+=1
    if i%11==0: f.write("\n")
f.close()
print("9-3=.doc Generated.")