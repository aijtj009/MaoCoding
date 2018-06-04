import random 
f=open("9876div12=()...().doc","w")
i=0
while i<360:
    j=random.randint(1000,9999)
    k=0
    while k%10==0:
        k=random.randint(11,99)
    f.write(str(j)+"/"+str(k)+"="+"(    )...(    )"+" "*4)        
    i+=1
    #if i%9==0: f.write("\n")
f.close()
print("9876div12=()...().doc Generated.")
