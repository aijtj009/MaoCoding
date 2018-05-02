import random 
f=open("1div2..1div99.doc","w")
for i in range(2,100):
    if i%10!=0: 
        f.write("1"+"/"+str(i)+"="+" "*(4+i))
        #f.write("\n")
f.close()
print("1div2..1div99.doc Generated.")