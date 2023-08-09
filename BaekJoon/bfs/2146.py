import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def print_board(board):
    for i in range(len(board)):
        print(board[i])
    print()
def mark(tmp, src, num):
    q = deque()
    q.append(src)
    tmp[src[0]][src[1]] = num

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n \
                    and board[nx][ny] == 1 and tmp[nx][ny] == 0:
                tmp[nx][ny] = num
                q.append((nx, ny))

def bridge(land, src, num):
    q = deque()
    q.append(src)

    tmp = [[0 for _ in range(n)] for _ in range(n)]
    tmp[src[0]][src[1]] = 1

    print(src)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and tmp[nx][ny] == 0:
                if land[nx][ny] == 0:
                    tmp[nx][ny] = tmp[x][y] + 1
                    q.append((nx, ny))
                    print_board(tmp)
                elif land[nx][ny] != 0 and land[nx][ny] != num:
                    return tmp[x][y] - 1
    return 10**9

n = int(sys.stdin.readline().strip())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

land = [[0 for _ in range(n)] for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and land[i][j] == 0:
            mark(land, (i, j), num)
            num += 1

min_len = 10**9
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            min_len = min(min_len, bridge(land, (i, j), land[i][j]))
            print(min_len)
            print("==================")
print(min_len)