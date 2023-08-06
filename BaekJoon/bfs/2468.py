import sys
from collections import deque
from copy import deepcopy

def bfs(board, src, h):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(src)
    board[src[0]][src[1]] = -1

    n = len(board)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h:
                board[nx][ny] = -1
                q.append((nx, ny))


n = int(sys.stdin.readline().strip())
height = []
max_h = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split(" ")))
    height.append(tmp)
    max_h = max(max_h, max(tmp))

max_safe = 0
for h in range(max_h):
    tmp = deepcopy(height)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > h:
                cnt += 1
                bfs(tmp, (i, j), h)
    max_safe = max(max_safe, cnt)

print(max_safe)