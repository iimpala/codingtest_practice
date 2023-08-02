import sys
from collections import deque


def bfs(r, c):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    area = 1

    q = deque()
    q.append((r, c))
    while q:
        curr = q.popleft()
        for i in range(4):
            next_x = curr[0] + dx[i]
            next_y = curr[1] + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m \
                    and graph[next_x][next_y] == 1 \
                    and not visited[next_x][next_y]:
                area += 1
                visited[next_x][next_y] = True
                q.append((next_x, next_y))

    return area


n, m = tuple(map(int, sys.stdin.readline().strip().split(" ")))
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))

visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            area = bfs(i, j)
            max_area = max(area, max_area)

print(cnt)
print(max_area)
