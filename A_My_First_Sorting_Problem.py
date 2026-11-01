a=int(input())
for i in range(a):
    x,y=input().split()
    if x>y:
        print(y,x)
    else:
        print(x,y)