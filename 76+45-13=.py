import random 
f=open("76+45-13=.doc","w")
i=0
while i<240:
    j=random.randint(11,99)
    k=random.randint(11,99)
    m=random.randint(11,99)
    ran=random.randint(0,1)
    if ran==0:
        n=j+k+m
        if n>99: continue
        f.write(str(n)+"-"+str(j)+"-"+str(k)+"="+" "*6)
    elif ran==1:
        n=j-k+m
        if n<10 or n>99 or j-k<=0: continue
        f.write(str(n)+"+"+str(k)+"-"+str(j)+"="+" "*6)              
    i+=1
    if i%6==0: f.write("\n\n")
f.close()
print("76+45-13=.doc Generated.")