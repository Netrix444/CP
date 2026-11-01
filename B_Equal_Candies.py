a = int(input())
for _ in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    d = min(c)
    ans = 0
    for x in c:
        ans += x - d
    print(ans)