import random 
f=open("19X37=.doc","w")
i=0
answers=[]
while i<126:
    j=random.randint(11,99)
    if j % 10 == 0: continue
    k=random.randint(11,99)
    if k % 10 == 0: continue
    n=j*k
    answers.append(n)
    f.write(str(j)+"X"+str(k)+"="+" "*5)
    i+=1
    if i%6==0: f.write("\n\n")
f.write(str(answers))
f.close()
print("19X37=.doc Generated.")