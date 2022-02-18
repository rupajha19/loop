#  if a number is divisible by its sum of digit then its called harshed number:

num=int(input("enter any number::"))
i=num
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
if num%sum==0:
    print("its harshad number:")
else:
    print("its not harshad number:")
