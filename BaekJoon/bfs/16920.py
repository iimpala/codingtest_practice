import sys
from collections import deque


def bfs(board, q, cnt, tmp):
    while q:
        if cnt[0] == 0:
            return

        x, y, k = q.popleft()

        if k == 0:
            tmp.append((x, y, move[board[x][y] - 1]))
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y]
                cnt[0] -= 1
                q.append((nx, ny, k-1))

def is_empty(qs):
    for i in range(p):
        if len(qs[i]) > 0:
            return False
    return True


n, m, p = map(int, sys.stdin.readline().strip().split(" "))
move = list(map(int, sys.stdin.readline().strip().split(" ")))
board = []
qs = [deque() for _ in range(p)]
cnt = [0]

for i in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for j in range(m):
        if line[j] == '.':
            cnt[0] += 1
            tmp.append(0)
        elif line[j] == "#":
            tmp.append(-1)
        else:
            c = int(line[j])
            qs[c - 1].append((i, j, move[c - 1]))
            tmp.append(c)
    board.append(tmp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while not is_empty(qs):
    if cnt[0] == 0:
        break

    tmp = []
    for i in range(p):
        bfs(board, qs[i], cnt, tmp)
        qs[i].extend(tmp)

result = [0 for _ in range(p)]
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            result[board[i][j] - 1] += 1

print(" ".join(map(str, result)))
