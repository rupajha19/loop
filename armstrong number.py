# armstrong number is that which sum of cube equal to its own digit.

num=int(input("enter any number::"))
i=num
sum=0
while i >0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if num==sum:
    print(num,"its hrshad number")
else:
    print(num,("its not harshad number"))





i=int(input("enter your number::"))
sum=0
j=i
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10);
    i=i//10
if j==sum:
        print("armstrong number")
else:
        print("not armstrong number")