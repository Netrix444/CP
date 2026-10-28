n=list(map(int,input().split()))
a=int(n[0])
b=int(n[1])
c=
    if a%b==0:
        print(a)
    else:
        for i in range(1,a):
            if a%i==0 and b%i==0:
                print(i)
