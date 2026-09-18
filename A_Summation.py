a=int(input())
b=input().split()
c=0
for i in range(a):
    c=c+int(b[i])
if c>=0:
    print(c)
else:
    print(-c)