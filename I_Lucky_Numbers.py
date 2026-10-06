x=int(input())
a=x//10
b=x%10
if a//b==0 or b//a==0:
    print("YES")
else:
    print("NO")
