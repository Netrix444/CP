while True:
    a = list(map(int, input().split()))
    if a[0] <= 0 or a[1] <= 0:
        break
    for i in range(min(a), max(a) + 1):
        print(i, end=" ")
    print(f"sum ={sum(range(min(a), max(a) + 1))}")
