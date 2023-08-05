import sys
from collections import deque
from copy import deepcopy


def bfs(board, srcs):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()

    for src in srcs:
        q.append(src)
        board[src[0]][src[1]] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) \
                    and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


t = int(sys.stdin.readline().strip())
tc = []
for _ in range(t):
    m, n = map(int, sys.stdin.readline().strip().split(" "))
    board = []
    fire = []
    src = tuple()
    for i in range(n):
        line = sys.stdin.readline().strip()
        tmp = []

        for j in range(m):
            if line[j] == "#":
                tmp.append(-1)
            elif line[j] == "*":
                tmp.append(-1)
                fire.append((i, j))
            elif line[j] == ".":
                tmp.append(0)
            elif line[j] == "@":
                tmp.append(0)
                src = (i, j)
        board.append(tmp)

    tc.append([board, fire, src])

result = []
for case in tc:
    board, fire, src = case

    fire_time = deepcopy(board)
    move_time = deepcopy(board)

    bfs(fire_time, fire)
    bfs(move_time, [src])

    n = len(board)
    m = len(board[0])
    tmp = []
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if board[i][j] == 0 and fire_time[i][j] >= 0 and move_time[i][j] > 0:
                    if fire_time[i][j] == 0 or fire_time[i][j] > move_time[i][j]:
                        tmp.append(move_time[i][j])
    if tmp:
        result.append(min(tmp))
    else:
        result.append("IMPOSSIBLE")

for r in result:
    print(r)

