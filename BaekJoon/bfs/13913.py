import sys
from collections import deque

def bfs(line, n):
    q = deque()
    q.append(n)
    line[n] = [1, n]

    while q:
        x = q.popleft()
        nx = 2 * x
        if nx <= 100000 and line[nx][0] == 0:
            line[nx] = [line[x][0] + 1, x]
            q.append(nx)

        for dx in [1, -1]:
            nx = x + dx
            if 0 <= nx <= 100000 and line[nx][0] == 0:
                line[nx] = [line[x][0] + 1, x]
                q.append(nx)

n, k = map(int, sys.stdin.readline().strip().split(" "))
line = [[0, 0] for _ in range(100001)]

bfs(line, n)

path = []
step, before = line[k]
now = k
path.append(now)

while now != n:
    path.append(before)
    now = before
    step, before = line[before]

print(line[k][0] - 1)
print(" ".join(map(str, reversed(path))))
