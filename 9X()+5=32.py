import random 
f=open("9X()+5=32.doc","w")
i=0
while i<240:
    j=random.randint(2,9)
    k=random.randint(2,9)
    m=random.randint(2,9)
    if random.randint(0,1)==0:
        n=j*k+m
        f.write(str(j)+"X"+"(   )"+"+"+str(m)+"="+str(n)+" "*6)        
    else:
        n=j*k-m
        if n<0: continue
        f.write(str(j)+"X"+"(   )"+"-"+str(m)+"="+str(n)+" "*6)
    i+=1
    if i%8==0: f.write("\n\n")
f.close()
print("9X()+5=32.doc Generated.")

