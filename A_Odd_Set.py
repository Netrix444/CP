import sys

def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  t = int(input_data[0])
  idx = 1
  out = []
  for _ in range(t):
    n = int(input_data[idx])
    idx += 1
    odds = sum(int(input_data[idx + i]) % 2 != 0 for i in range(2 * n))
    idx += 2 * n
    out.append("Yes" if odds == n else "No")
  print("\n".join(out))
if __name__ == "__main__":
  solve()