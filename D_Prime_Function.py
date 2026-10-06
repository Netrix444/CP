t = int(input())
for _ in range(t):
    n = int(input())
    if n < 2:
        print("NO")
        continue
    is_p = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_p = False
            break
    print("YES" if is_p else "NO")