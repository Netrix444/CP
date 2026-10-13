a=int(input())
for _ in range(a):
    b=list(map(int,input().split()))
    c=int(b[0])
    d=int(b[1])
    if c<d:
        c=((c-1)*c)//2
        d=(d*(d+1))//2
        print(int(d-c))
    else:
        c=(c*(c+1))//2
        d=((d-1)*d)//2
        print(int(c-d))

