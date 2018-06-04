firstPage=2
lastPage=21
j=0
i=list(range(firstPage,lastPage+1))
firstSide=i[0::2]
secondSide=i[1::2]
k=0
while k<len(firstSide):
    if k%10==9:
        print(firstSide[k])
    else:
        print(firstSide[k],end=",")
    k+=1
k=0
print("")
while k<len(secondSide):
    if k%10==9:
        print(secondSide[k])
    else:
        print(secondSide[k],end=",")
    k+=1    