import random 
f=open("3+3+3+3=.doc","w")
i=0
while i<261:
    j=random.randint(2,9)
    k=random.randint(2,9)
    n=j*k
    for m in range(k):
        if m==0:
            f.write(str(j))
        else:
            f.write("+"+str(j))
    f.write("="+"       ") 
    i+=1
    if i%9==0: f.write("\n")
f.close()
print("3+3+3+3=.doc Generated.")