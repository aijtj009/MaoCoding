import random 
f=open("2X7+4.doc","w")
i=0
while i<180:
    j=random.randint(2,7)
    k=random.randint(2,7)
    m=random.randint(2,7)
    n=k*j+m
    f.write(str(j)+"X"+str(k)+"+"+str(m)+"=      ")        
    i+=1
    if i%6==0: f.write("\n\n")
f.close()
print("2X7+4.doc Generated.")

