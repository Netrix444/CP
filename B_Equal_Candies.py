a = int(input())
for i in range(a):
    b = int(input())
    c= list(map(int, input().split()))
    d = max(c)
    ans = 0
    for x in c:
        ans += d - x
    print(ans)