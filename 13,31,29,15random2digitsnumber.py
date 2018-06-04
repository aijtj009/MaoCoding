import random 
f=open("13,31,29,15random2digitsnumber.doc","w")
i=0
while i<315:
    if random.randint(0,1)==1:
        j=random.randint(11,19)        
    else:
        j=random.randint(20,99)
    f.write(str(j)+":"+" "*12)
    i+=1
    if i%6==0: f.write("\n\n")
f.close()
print("13,31,29,15random2digitsnumber.doc Generated.")