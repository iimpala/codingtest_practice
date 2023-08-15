import sys
from collections import deque

t = int(sys.stdin.readline().strip())
tc = []

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    board = []
    start = []
    key = []
    for i in range(n):
        tmp = list(sys.stdin.readline().strip())
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1):
                if tmp[j].islower():
                    key.append(tmp[j])
                    tmp[j] = "."
                    start.append((i, j))

                elif tmp[j] != "*":
                    start.append((i, j))

        board.append(tmp)

    key.extend(list(sys.stdin.readline().strip()))
    tc.append((board, start, key))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = []
for board, start, key in tc:
    cnt = 0
    n, m = len(board), len(board[0])
    wait = {chr(ord('A') + i): [] for i in range(26)}

    q = deque()
    for x, y in start:
        if board[x][y] == ".":
            board[x][y] = "#"
            q.append((x, y))
        elif board[x][y] == "$":
            cnt += 1
            board[x][y] = "#"
            q.append((x, y))
        elif board[x][y].isupper():
            if board[x][y].lower() not in key:
                wait[board[x][y]].append((x, y))
            else:
                board[x][y] = "#"
                q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "*" and board[nx][ny] != "#":
                if board[nx][ny] == ".":
                    board[nx][ny] = "#"
                    q.append((nx, ny))

                elif board[nx][ny] == "$":
                    cnt += 1
                    board[nx][ny] = "#"
                    q.append((nx, ny))

                elif board[nx][ny].isupper():
                    if board[nx][ny].lower() in key:
                        board[nx][ny] = "#"
                        q.append((nx, ny))
                    else:
                        wait[board[nx][ny]].append((nx, ny))

                elif board[nx][ny].islower():
                    key.append(board[nx][ny])

                    for a, b in wait[board[nx][ny].upper()]:
                        board[a][b] = "#"
                        q.append((a, b))

                    board[nx][ny] = "#"
                    q.append((nx, ny))

    result.append(cnt)

for r in result:
    print(r)
