import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(" "))
edges = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, nx, ny = map(int, sys.stdin.readline().strip().split(" "))
    edges[x-1][y-1].append((nx-1, ny-1))

visited = [[False for _ in range(n)] for _ in range(n)]
light = [[False for _ in range(n)] for _ in range(n)]
adj = [[[] for _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((0, 0))

light[0][0] = True
cnt = 1
while q:
    x, y = q.popleft()
    if visited[x][y]:
        continue

    visited[x][y] = True

    for nx, ny in edges[x][y]:
        if light[nx][ny]:
            continue
        light[nx][ny] = True
        cnt += 1

        for i in range(4):
            adj_x, adj_y = nx + dx[i], ny + dy[i]
            if 0 <= adj_x < n and 0 <= adj_y < n:
                if visited[adj_x][adj_y]:
                    q.append((nx, ny))
                    break
                else:
                    adj[adj_x][adj_y].append((nx, ny))

    q.extend(adj[x][y])

print(cnt)
