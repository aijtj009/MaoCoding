import random 
f=open("123+456+789=.doc","w")
i=0
n=[]
while i<150:
    j=random.randint(101,999)
    k=random.randint(101,999)
    m=random.randint(101,999)
    // 个位三个数相加 和 十位三个数相加 不能进2，也就是说不能为二十几
    if int(str(j)[2])+int(str(k)[2])+int(str(m)[2])>19: continue
    if int(str(j)[1])+int(str(k)[1])+int(str(m)[1])>19: continue
    n.append(j+k+m)    
    f.write(str(j)+"+"+str(k)+"+"+str(m)+"="+" "*6)
    i+=1
    if i%5==0: f.write("\n\n")
f.write(str(n))
f.close()
print("123+456+789=.doc Generated.")