
i=int(input("enetr the number::"))
rev=0
x=i
while i>0:
    rev=(rev*10)+rev%10
    i=i//10
if i==rev:
    print("palindrome")
else:
    print("not palindrome")
