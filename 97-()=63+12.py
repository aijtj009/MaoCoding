import random 
f=open("97-()=63+12.doc","w")
i=0
while i<180:
    j=random.randint(11,99)
    k=random.randint(11,99)
    m=random.randint(11,99)
    ran=random.randint(0,3)
    if ran==0:
        n=j+k+m
        if n>99: continue
        if random.randint(0,1)==1:
            f.write(str(n)+"-"+str(k)+"="+str(j)+"+"+"(   )"+"    ")
        else:
            f.write(str(j)+"+"+"(   )"+"="+str(n)+"-"+str(k)+"    ")
    elif ran==1:
        n=j-k-m
        if n<10 or n>99 or j-k<=0: continue
        if random.randint(0,1)==1:
            f.write(str(k)+"+"+str(n)+"="+str(j)+"-"+"(   )"+"    ")
        else:
            f.write(str(j)+"-"+"(   )"+"="+str(k)+"+"+str(n)+"    ")
    elif ran==2:
        n=j-k+m
        if n<10 or n>99 or j-k<=0: continue
        if random.randint(0,1)==1:
            f.write(str(n)+"+"+str(k)+"="+str(j)+"+"+"(   )"+"    ")
        else:
            f.write(str(j)+"+"+"(   )"+"="+str(n)+"+"+str(k)+"    ")      
    else:
        n=j+k-m
        if n<10 or n>99 or n-k<=0: continue
        if random.randint(0,1)==1:
            f.write(str(n)+"-"+str(k)+"="+str(j)+"-"+"(   )"+"    ")
        else:
            f.write(str(j)+"-"+"(   )"+"="+str(n)+"-"+str(k)+"    ")        
    i+=1
    if i%5==0: f.write("\n\n")
f.close()
print("97-()=63+12.doc Generated.")



