#to find whethwe num is a prime or not
s=int(input("enter a number"))
print(s)
count=0
for i in range(2,s):
    if (s%i==0):
        count+=1
if (count==0):
    print("s is a prime")
else:
    print("s is not a prime")
    
    
