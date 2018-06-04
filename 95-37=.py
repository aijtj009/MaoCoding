import random 
f=open("95-37=.doc","w")
i=0
while i<800:
    j=random.randint(11,99)
    k=random.randint(11,99)
    n=j-k
    if n<=0 or j % 10 == 0 or k % 10 == 0: continue
    f.write(str(j)+"-"+str(k)+"="+" "*4)
    i+=1
    if i%9==0: f.write("\n")
f.close()
print("95-37=.doc Generated.")
