a=list(map(int,input().split()))
b=a[0]
c=a[1]
d=a[2]
cost=0
for i in range(d+1):
    cost=cost+(b*i)
    r=cost-c
if r>0:
    print(r)
else:
    print(0)
