import sys
from collections import deque

def bfs(graph, visited, start):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                    graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


t = int(sys.stdin.readline().strip())
tc = []
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split(" "))
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, sys.stdin.readline().strip().split(" "))
        graph[x][y] = 1
    tc.append(graph)

result = []
for graph in tc:
    cnt = 0
    n = len(graph)
    m = len(graph[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(graph, visited, (i, j))

    result.append(cnt)

for r in result:
    print(r)
