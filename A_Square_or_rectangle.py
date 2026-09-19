a=int(input())
for b in range(a):
    b=input().split()
    if int(b[0])==int(b[1]):
        print("Square")
    else:
        print("Rectangle")