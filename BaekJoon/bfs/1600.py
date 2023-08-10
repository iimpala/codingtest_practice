import sys
from collections import deque


def bfs(cube):
    horse = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    monkey = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append((0, 0, 0))

    for i in range(k + 1):
        cube[i][0][0] = 1

    while q:
        x, y, hop = q.popleft()

        if hop < k:
            for dx, dy in horse:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and cube[hop + 1][nx][ny] == 0:
                    cube[hop + 1][nx][ny] = cube[hop][x][y] + 1
                    q.append((nx, ny, hop + 1))

        for dx, dy in monkey:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and cube[hop][nx][ny] == 0:
                cube[hop][nx][ny] = cube[hop][x][y] + 1
                q.append((nx, ny, hop))


k = int(sys.stdin.readline().strip())
m, n = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

dist = [[row[:] for row in board] for _ in range(k + 1)]
bfs(dist)

tmp = []
for i in range(k + 1):
    if dist[i][n-1][m-1] > 0:
        tmp.append(dist[i][n-1][m-1] - 1)

if len(tmp) > 0:
    print(min(tmp))
else:
    print(-1)
