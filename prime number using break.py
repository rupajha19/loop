i=0
while i<100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print("its prime number:",i)
    if i==17:
        break
    else:
        print("its not prime number::",i)
    i+=1    








    
