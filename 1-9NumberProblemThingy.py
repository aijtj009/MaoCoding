numbers = [0,0,0,0,0,0,0,0,0,0]
for i in range(1000,10000):
    numbers[0]=i//1000
    numbers[1]=(i-numbers[0]*1000)//100
    numbers[2]=(i-(numbers[0]*1000+numbers[1]*100))//10
    numbers[3]=(i-(numbers[0]*1000+numbers[1]*100+numbers[2]*10))//1
    j=i*99
    numbers[4]=j//100000
    numbers[5]=(j-numbers[4]*100000)//10000
    numbers[6]=(j-(numbers[4]*100000+numbers[5]*10000))//1000
    numbers[7]=(j-(numbers[4]*100000+numbers[5]*10000+numbers[6]*1000))//100
    numbers[8]=(j-(numbers[4]*100000+numbers[5]*10000+numbers[6]*1000+numbers[7]*100))//10
    numbers[9]=j-(numbers[4]*100000+numbers[5]*10000+numbers[6]*1000+numbers[7]*100+numbers[8]*10)
    toobad=False
    for k in range(10):
        count=0
        for m in range(10):
            if numbers[m]==k:
                count+=1
        if count!=1:
            toobad=True
            break
    if not toobad:
        print(j,"/",i,"=99")
    