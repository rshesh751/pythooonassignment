#to find the numbres position added up to give target value
"""list numbers +1 """
m=[]
n=int(input("number of digits you will enter"))
for i in range(n):
    p=int(input())
    m+=[p]
s=""
for i in range(len(m)):
    s=s+str(m[i])
    k=int(s)+1
k=str(k)
list=[]
for i in k:
    list+=[i]
print(list)