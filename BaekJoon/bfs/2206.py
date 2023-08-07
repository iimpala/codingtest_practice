import sys
from collections import deque

def bfs(board, dist, src):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append((src[0], src[1], 0))

    dist[src[0]][src[1]][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == n-1 and y == m-1:
            return dist[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and dist[nx][ny][w] == 0:
                    dist[nx][ny][w] = dist[x][y][w] + 1
                    q.append((nx, ny, w))

                elif board[nx][ny] == 1 and w == 0:
                    dist[nx][ny][w+1] = dist[x][y][w] + 1
                    q.append((nx, ny, w+1))
    return -1


n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
for i in range(n):
    row = list(map(int, list(sys.stdin.readline().strip())))
    board.append(row)

dist = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(bfs(board, dist, (0, 0)))
