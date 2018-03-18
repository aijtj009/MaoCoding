numbers = [0,0,0,0,0,0,0,0,0,0]
for i in range(100,1000):
    numbers[0]=i//100
    numbers[1]=(i-numbers[0]*100)//10
    numbers[2]=(i-(numbers[0]*100+numbers[1]*10))
    j=i*2
    numbers[3]=j//100
    numbers[4]=(j-numbers[3]*100)//10
    numbers[5]=(j-(numbers[3]*100+numbers[4]*10))
    toobad=False
    for k in range(4,10):
        count=0
        for m in range(6):
            if numbers[m]==k:
                count+=1
        if count!=1:
            toobad=True
            break
    if not toobad:
        print(j,"/",i,"=2")
    
