import sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    rope.append(int(sys.stdin.readline()))

rope.sort()
w = 0

for k in rope:
    w = max(w, n * k)
    n -= 1

print(w)
