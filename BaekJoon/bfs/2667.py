import sys
from collections import deque


def bfs(board, src):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append(src)
    board[src[0]][src[1]] = 0

    cnt = 0
    n = len(board)
    while q:
        cnt += 1
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))
    return cnt


n = int(sys.stdin.readline().strip())
town = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for c in line:
        tmp.append(int(c))
    town.append(tmp)

result = []
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            result.append(bfs(town, (i, j)))

result.sort()
print(len(result))

for r in result:
    print(r)