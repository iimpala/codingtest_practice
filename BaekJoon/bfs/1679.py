import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split(" "))

q = deque()
visited = [False for _ in range(100001)]

q.append((n, 0))

ans = 0
while q:
    c_pos, step = q.popleft()
    visited[c_pos] = True

    if c_pos == k:
        ans = step
        break

    n_pos = [c_pos + 1, c_pos - 1, c_pos * 2]
    for pos in n_pos:
        if 0 <= pos <= 100000 and not visited[pos]:
            q.append((pos, step + 1))

print(ans)
