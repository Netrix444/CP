a = int(input())
b = list(map(int, input().split()))

max_count = 0
for num in b:
    count = 0
    while num % 2 == 0:
        num //= 2
        count += 1
    max_count = max(max_count, count)

print(max_count)
