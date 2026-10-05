a=int(input())
b=list(map(int,input().split()))
b.sort()
for i in range(len(b)):
    print(b[i],end=' ')
