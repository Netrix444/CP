a=int(input())
for b in range(1,a):
    b=int(input())
    if b==2:
        print("YES")
    elif b>=1:
        print("NO")
    else:
        for i in range(2,b):
            if b/i==0:
                print("NO")
            else:
                print("YES")