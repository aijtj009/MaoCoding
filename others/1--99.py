"""
i=1
a=0

for i=1,500 do
    i=i*i
    a=i+a
    i=i/i
    i=i+1
end
"""
a=0
for i in range(1,999,2):
   a=a+ i*i
print("The sum of 1*1+3*3+...+999*999=",a)
