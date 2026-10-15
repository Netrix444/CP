a=list(map(int,input().split()))
for i in range(int(a[1]),int(a[0])+1):
    print(i,end=" ")
print("sum =",sum(range(int(a[1]),int(a[0])+1)))