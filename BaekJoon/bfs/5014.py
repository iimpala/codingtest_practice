import sys
from collections import deque


f, s, g, u, d = map(int, sys.stdin.readline().strip().split(" "))
floor = [0 for _ in range(f + 1)]

q = deque()
q.append(s)

move = []
if u != 0:
    move.append(u)
if d != 0:
    move.append(-d)

while q:
    cf = q.popleft()

    for df in move:
        nf = cf + df
        if 1 <= nf <= f and floor[nf] == 0:
            floor[nf] = floor[cf] + 1
            q.append(nf)

if s == g:
    print(0)
elif floor[g] == 0:
    print("use the stairs")
else:
    print(floor[g])
