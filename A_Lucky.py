a=int(input())
for b in range(a):
    b=input()
    c=sum(int(digit) for digit in b[:3])
    d=sum(int(digit) for digit in b[3:])
    if c==d:
        print("YES")
    else:
        print("NO")