a=int(input())
b=f"{a//10} {a%10}"
if int(b[0])%int(b[2])==0 or int(b[2])%int(b[0])==0:
    print("YES")
else:
    print("NO")