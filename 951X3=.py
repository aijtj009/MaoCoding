import random 
f=open("951X3=.doc","w")
i=0
answers=[]
while i<126:
    j=random.randint(101,999)
    if j % 10 == 0: continue
    k=random.randint(2,9)
    n=j*k
    answers.append(n)
    f.write(str(j)+"X"+str(k)+"="+" "*5)
    i+=1
    if i%6==0: f.write("\n\n")
f.write(str(answers))
f.close()
print("951X3=.doc Generated.")