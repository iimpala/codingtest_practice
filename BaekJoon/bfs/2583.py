import sys
from collections import deque


def bfs(space, src):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(src)
    space[src[0]][src[1]] = False

    area = 0
    n = len(space)
    m = len(space[0])
    while q:
        area += 1
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and space[nx][ny]:
                space[nx][ny] = False
                q.append((nx, ny))

    return area


n, m, k = map(int, sys.stdin.readline().strip().split(" "))
space = [[True for _ in range(m)] for _ in range(n)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().strip().split(" "))
    for i in range(x1, x2):
        for j in range(y1, y2):
            space[i][j] = False

result = []
for i in range(n):
    for j in range(m):
        if space[i][j]:
            result.append(bfs(space, (i, j)))

result.sort()
print(len(result))
print(" ".join(map(str, result)))
