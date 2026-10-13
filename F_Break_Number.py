a = int(input())
b = list(map(int, input().split()))
output = 0
for i in b:
    c = 0
    while i % 2 == 0:
        i //= 2
        c += 1
    output= max(output,c)
print(output)
