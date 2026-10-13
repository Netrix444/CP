a=int(input())
for _ in range(a):
    b=list(map(int,input().split()))
    c=int(b[0])
    d=int(b[1])
    if c<d:
        c=((int(b[0])-1)*int(b[0]))/2
        d=(int(b[1])*(int(b[1]+1)))/2
        print(int(d-c))
    else:
        c=(int(b[0])*(int(b[0])+1))/2
        d=((int(b[1])-1)*int(b[1]))/2
        print(int(c-d))

