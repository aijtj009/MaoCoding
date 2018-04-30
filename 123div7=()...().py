import random 
f=open("123div7=()...().doc","w")
i=0
while i<360:
    j=random.randint(100,299)
    k=random.randint(3,9)
    f.write(str(j)+"/"+str(k)+"="+"(  )...(  )"+" "*4)        
    i+=1
    #if i%9==0: f.write("\n")
f.close()
print("123div7=()...().doc Generated.")
