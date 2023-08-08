import sys
from collections import deque

def bfs(board):
    tmp = [row[:] for row in board]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if tmp[i][j] != 0:
                cnt += 1
                q = deque()
                q.append((i, j))
                tmp[i][j] = 0

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] != 0:
                            tmp[nx][ny] = 0
                            q.append((nx, ny))

    return cnt

def melt(board):
    tmp = [row[:] for row in board]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for x in range(n):
        for y in range(m):
            if board[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                        cnt += 1

                if tmp[x][y] >= cnt:
                    tmp[x][y] -= cnt
                else:
                    tmp[x][y] = 0

    return tmp

n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

year = 0
while True:
    cnt = bfs(board)
    if cnt != 1:
        break
    year += 1
    board = melt(board)

if cnt == 0:
    print(0)
else:
    print(year)
