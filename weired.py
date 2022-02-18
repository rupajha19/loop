n=int(input("enter the number"))
i=1
while i<=n:
    if i%2!=0:
        print(i,"weird")
    i=i+1

for i in range (2,5):
    if i%2==0:
        print(i,"not weird")


for i in range (6,20):
    if i%2==0:
        print(i,"weird")


while i<=n:
    if i%2==0 and i>20:
        print(i,"not weird")
    i=i+1
