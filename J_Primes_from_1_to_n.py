n=int(input())
for i in range(2,n+1):
    prime = 0
    for b in range(1,i+1):
        if i % b == 0:
            prime += 1
    if prime == 2:
        print(i, end=" ")