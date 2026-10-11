t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    if s > n * (n + 1) // 2:
        print(-1)
    else:
        ans = []
        for i in range(n, 0, -1):
            if s >= i:
                ans.append(i)
                s -= i

        if s == 0:
            print(*ans)
        else:
            print(-1)