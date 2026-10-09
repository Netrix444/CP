a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    if int(b[i])<10:
        print(f"A[{i}] = {b[i]}")