a=int(input())
for b in range(a):
    b=int(input())
    if b==0:
        print(1)
    else:
        for i in range(1,b):
            b=b*i
        print(b)
  