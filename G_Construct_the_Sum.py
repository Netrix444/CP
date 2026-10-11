import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); s = int(data[idx + 1]); idx += 2
        if s > n * (n + 1) // 2:
            out.append("-1")
            continue
        # largest k such that 1+2+...+k <= s (and k <= n)
        k = 0
        total = 0
        while k < n and total + k + 1 <= s:
            k += 1
            total += k
        r = s - total  # leftover, 0 <= r <= k
        res = []
        for i in range(k, 0, -1):
            # add 1 to the r largest numbers
            res.append(i + 1 if i > k - r else i)
        out.append(" ".join(map(str, res)))
    print("\n".join(out))

main()