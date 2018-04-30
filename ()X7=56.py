import random 
f=open("()X7=56.doc","w")
i=0
while i<360:
    j=random.randint(2,7)
    k=random.randint(2,7)
    n=j*k
    f.write("(  )"+"X"+str(k)+"="+str(n)+"    ")        
    i+=1
    if i%9==0: f.write("\n")
f.close()
print("()X7=56.doc Generated.")
