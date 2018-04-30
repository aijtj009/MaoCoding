import random 
f=open("97-()+24=63.doc","w")
i=0
while i<180:
    j=random.randint(11,100)
    k=random.randint(11,100)
    m=random.randint(11,100)
    ran=random.randint(0,3)
    if ran==0:
        n=j+k+m
        if n>99: continue
        f.write(str(j)+"+"+"(   )"+"+"+str(k)+"="+str(n)+"  ")
    elif ran==1:
        n=j-k-m
        if n<10 or n>99 or j-k<=0: continue
        f.write(str(j)+"-"+"(   )"+"-"+str(k)+"="+str(n)+"  ")
    elif ran==2:
        n=j-k+m
        if n<10 or n>99 or j-k<=0: continue
        f.write(str(j)+"+"+"(   )"+"-"+str(k)+"="+str(n)+"  ")           
    else:
        n=j+k-m
        if n<10 or n>99: continue
        f.write(str(j)+"-"+"(   )"+"+"+str(k)+"="+str(n)+"  ")        
    i+=1
    if i%5==0: f.write("\n\n")
f.close()
print("97-()+24=63.doc Generated.")


