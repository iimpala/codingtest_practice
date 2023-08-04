import sys
from collections import deque

def bfs(paint, visited, start, color):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and paint[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

n = int(sys.stdin.readline().strip())
paint_normal = []
paint_week = []
for _ in range(n):
    row = sys.stdin.readline().strip()
    paint_normal.append(list(row))
    paint_week.append(list(row.replace("G", "R")))

normal = 0
week = 0
visited_normal = [[False for _ in range(n)] for _ in range(n)]
visited_week = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            normal += 1
            bfs(paint_normal, visited_normal, (i, j), paint_normal[i][j])

        if not visited_week[i][j]:
            week += 1
            bfs(paint_week, visited_week, (i, j), paint_week[i][j])

print(f"{normal} {week}")
