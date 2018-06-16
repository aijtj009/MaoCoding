import random 
f=open("456+789-123=.doc","w")
i=0
n=[]
while i<150:
    j=random.randint(101,999)
    k=random.randint(101,999)
    m=random.randint(101,999)
    result=j+k-m
    if result<1: continue
    n.append(result)    
    f.write(str(j)+"+"+str(k)+"-"+str(m)+"="+" "*6)
    i+=1
    if i%5==0: f.write("\n\n")
f.write(str(n))
f.close()
print("456+789-123=.doc Generated.")
