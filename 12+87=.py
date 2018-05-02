import random 
f=open("12+87=.doc","w")
i=0
while i<315:
    j=random.randint(10,99)
    k=random.randint(10,99)
    n=j+k
    if n>99: continue
    f.write(str(j)+"+"+str(k)+"="+" "*4)
    i+=1
    if i%9==0: f.write("\n\n")
f.close()
print("12+87=.doc Generated.")