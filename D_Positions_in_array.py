a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if i%2==0:
        c=c+b[i]
print(c)