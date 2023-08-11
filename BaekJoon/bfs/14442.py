import sys
from collections import deque


def bfs(cube):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0, 0))
    for plane in cube:
        plane[0][0] = 1

    while q:
        x, y, hop = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    if cube[hop][nx][ny] == 0:
                        cube[hop][nx][ny] = cube[hop][x][y] + 1
                        q.append((nx, ny, hop))
                elif hop + 1 <= k and cube[hop+1][nx][ny] == 0:
                    cube[hop+1][nx][ny] = cube[hop][x][y] + 1
                    q.append((nx, ny, hop+1))

n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for c in line:
        if c == '1':
            tmp.append(-1)
        else:
            tmp.append(0)
    board.append(tmp)

dist = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]

bfs(dist)

result = []
for i in range(k+1):
    if dist[i][n-1][m-1] != 0:
        result.append(dist[i][n-1][m-1])

if len(result) == 0:
    print(-1)
else:
    print(min(result))
