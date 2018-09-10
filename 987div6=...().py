import random 
f=open("987div6=()...().doc","w")
i=0
answer=[]
while i<144:
    j=random.randint(100,999)
    k=0
    while k%10==0:
        k=random.randint(2,9)
    f.write(str(j)+"/"+str(k)+"="+"(    )...(    )"+" "*5)
    i+=1
    answer.append(j//k)
    answer.append(j%k)
    if i%3==0: f.write("\n")
f.write("\n")
f.write(str(answer))
f.close()
print("987div6=()...().doc Generated.")
