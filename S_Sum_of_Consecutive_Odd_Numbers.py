t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    total = 0
    for n in range(x + 1, y):
        if n % 2 == 1:
            total += n
    print(total)