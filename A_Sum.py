a=int(input())
for b in range(a):
    b=list(map(int,input().split()))
    if int(b[0])+int(b[1])==int(b[2]):
        print("YES")
    elif int(b[0])==int(b[1])+int(b[2]):
        print("YES")
    elif int(b[2])+int(b[0])==int(b[1]):
        print("YES")
    else:
        print("NO")

