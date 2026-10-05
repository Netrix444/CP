a=int(input())
b=input().split()
c=len(b)
for i in range(a):
    if int(b[i])>0:
        print(1,end=" ")
    elif int(b[i])==0:
        print(0,end=" ")
    elif int(b[i])<0:
        print(2,end=" ")