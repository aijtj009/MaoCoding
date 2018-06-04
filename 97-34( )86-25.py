import random 
f=open("97-34( )86-25.doc","w")
i=0
while i<315:
    j=random.randint(10,99)
    k=random.randint(10,99)
    p=random.randint(10,99)
    q=random.randint(10,99)    
    n=j-k
    r=p-q
    if n<=0 or r<=0 or abs(n-r)>9: continue
    f.write(str(j)+"-"+str(k)+"(  )"+str(p)+"-"+str(q)+" "*4)
    i+=1
    if i%5==0: f.write("\n\n")
f.close()
print("97-34( )86-25.doc Generated.")