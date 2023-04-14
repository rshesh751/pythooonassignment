#fibonacci series
t = 3
n = int(input("Enter no of terms"))
sum1 = 0
sum2 = 1
print("0 1",end=" ")

while t <= n:
    t += 1
    sum3 = sum1 + sum2
    sum1 = sum2
    sum2 = sum3
    print(sum3,end=" ")

