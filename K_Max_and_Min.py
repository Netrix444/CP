'''a=input().split()
if int(a[0])<=int(a[1]) and int(a[0])<=int(a[2]):
    print(int(a[0]),max(a))
elif int(a[1])<=int(a[0]) and int(a[1])<=int(a[2]):
    print(int(a[1]),max(a))
else:
    int(a[2])<=int(a[0]) and int(a[2])<=int(a[1])
    print(int(a[2]),max(a))
'''

a=input().split()
b=list(map(int,a))
print(min(b),end=' ')
print(max(b))