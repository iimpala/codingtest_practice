import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()

t = 0
for i in range(n):
    t += p[i] * (n-i)

print(t)