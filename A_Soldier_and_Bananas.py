a=list(map(int,input().split()))
s=0
d=0
for i in range(int(a[2])+1):
    b=int(a[0])*i
    s=s+b
    d=s-int(a[1])
print(d)
if int(a[1])>=s:
    print(0)