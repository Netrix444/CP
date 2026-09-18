n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n,2*n+1):
    if n%2==0:
        print(" "*(i-n)+"*"*((2*n)-(i-n//2)-(i-(2*n+(n-2))//2)))
    else:
        print(" "*(i-n)+"*"*((2*n+1)-(i-n//2)-(i-(2*n+(n-2))//2)))