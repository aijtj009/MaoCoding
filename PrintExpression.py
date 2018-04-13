import random 
f=open("2X9+5.doc","w")
i=0
while i<180:
    j=random.randint(2,9)
    k=random.randint(2,9)
    m=random.randint(2,9)
    if random.randint(0,1)==0:
        n=i*j+m
        f.write(str(j)+"X"+str(k)+"+"+str(m)+"=      ")        
    else:
        n=i*j-m
        if n<0: continue
        f.write(str(j)+"X"+str(k)+"-"+str(m)+"=      ")
    i+=1
    if i%6==0: f.write("\n\n")
f.close()
print("2X9+5.doc Generated.")
