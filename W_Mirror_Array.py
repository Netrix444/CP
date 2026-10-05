a= input().split()
for i in range(int(a[0])):
    b=list(map(int,input().split()))
    b.reverse()
    print(*b)