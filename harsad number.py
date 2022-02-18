num=int(input("enter your number::"))
i=num
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
if num%sum==0:
    print(num," is harshad number")
else:
    print(num,"is not harshad number")