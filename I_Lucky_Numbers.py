x=int(input())
a=int(x//10)
b=int(x%10)
if (b!=0 and a%b==0) or (b%9a==0 and a!=0):
    print("YES")
else:
    print("NO")