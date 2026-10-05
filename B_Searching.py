a=int(input())
b=input().split()
c=int(input())
for i in range(a):
    if c==int(b[i]):
        print(array.find(c))
    else:
        print(-1)
