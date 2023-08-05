import sys
from collections import deque

def bfs(n, board, src):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    q = deque()
    q.append(src)

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


t = int(sys.stdin.readline().strip())
tc = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    src = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    dst = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    tc.append([n, src, dst])

result = []
for case in tc:
    n, src, dst = case
    if src == dst:
        result.append(0)
        continue

    board = [[0 for _ in range(n)] for _ in range(n)]
    bfs(n, board, src)
    result.append(board[dst[0]][dst[1]])

for r in result:
    print(r)
