num=int(input("enter your number::"))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(num,"is prime number")
else:
    print(num,"is not prime number")
