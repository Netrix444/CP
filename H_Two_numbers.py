a=input().split()
b=int(a[0])//int(a[1])
c=int(a[0])/int(a[1])
print("floor",int(a[0]),"/",int(a[1]),"=",b)
if c>b:
    print("ceil",int(a[0]),"/",int(a[1]),"=",b+1)
else:
    print("ceil",int(a[0]),"/",int(a[1]),"=",b)
if c==b+0.5 :
    if b%2==0:
        print("round",int(a[0]),"/",int(a[1]),"=",round(c)+1)
    else:
        print("round",int(a[0]),"/",int(a[1]),"=",round(c))
else: 
    print("round",int(a[0]),"/",int(a[1]),"=",round(c))