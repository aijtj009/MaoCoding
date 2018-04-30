import random 
f=open("9X()=81.doc","w")
i=0
while i<261:
    j=random.randint(2,9)
    k=random.randint(2,9)
    n=j*k
    f.write("(  )"+"X"+str(k)+"="+str(n)+"    ")        
    i+=1
    if i%9==0: f.write("\n\n")
f.close()
print("9X()=81.doc Generated.")