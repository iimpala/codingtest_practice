import sys
from collections import deque

# def print_board(board):
#     for i in range(len(board)):
#         print(board[i])
#     print()

# def bfs(dist, visited):
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     q = deque()
#     q.append((0, 0, 0))
#
#     dist[0][0][0] = 1
#
#     while q:
#         x, y, t = q.popleft()
#
#         if x == n-1 and y == m-1:
#             return
#
#         if t == 0:
#             nt = 1
#         else:   # 밤
#             nt = 0
#
#         hop = visited[x][y][t]
#
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#
#                 if t == 0:   # 낮
#                     if board[nx][ny] == 0:  # 길
#                         if dist[nx][ny][nt] == 0 or visited[nx][ny][nt] > hop:  # 이동(낮 -> 밤) - 낮에 갔으면 굳이 밤에 안감
#                             dist[nx][ny][nt] = dist[x][y][t] + 1
#                             visited[nx][ny][nt] = visited[x][y][t]  # 벽 안부숨
#                             q.append((nx, ny, nt))
#
#                     elif hop + 1 <= k and (dist[nx][ny][nt] == 0 or visited[nx][ny][nt] > hop):   # hop(낮 -> 밤)
#                         dist[nx][ny][nt] = dist[x][y][t] + 1
#                         visited[nx][ny][nt] = visited[x][y][t] + 1
#                         q.append((nx, ny, nt))
#
#                 else:   # 밤
#                     if board[nx][ny] == 0:  # 길
#                         if dist[nx][ny][nt] == 0 or visited[nx][ny][nt] > hop:  # 이동(낮, 밤 무관)
#                             dist[nx][ny][nt] = dist[x][y][t] + 1
#                             visited[nx][ny][nt] = visited[x][y][t]
#                             q.append((nx, ny, nt))
#
#         if t == 1:
#             if dist[x][y][nt] == 0:
#                 dist[x][y][nt] = dist[x][y][t] + 1    # stay
#                 visited[x][y][nt] = visited[x][y][t]
#                 q.append((x, y, nt))
#
#         # print("===================")
#         # print(x, y, t)
#         # print_board(dist)
#         # print_board(visited)


import sys
from collections import deque


def bfs():
    if n == m == 1:
        return 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    q.append((0, 0, 0))
    res = 1

    night = False
    while q:
        for _ in range(len(q)):
            x, y, hop = q.popleft()

            if x == n-1 and y == m-1:
                return res

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if visited[nx][ny] <= hop:
                    continue

                if not night:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = hop
                        q.append((nx, ny, hop))
                    else:
                        if hop >= k:
                            continue
                        visited[nx][ny] = hop
                        q.append((nx, ny, hop + 1))
                else:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = hop
                        q.append((nx, ny, hop))
                    else:
                        q.append((x, y, hop))
        night = not night
        res += 1

    return -1

n, m, k = map(int, sys.stdin.readline().strip().split(" "))
board = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for c in line:
        tmp.append(int(c))
    board.append(tmp)

visited = [[k+1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

print(bfs())
