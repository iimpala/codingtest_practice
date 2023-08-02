import sys
from collections import deque

n, m = tuple(map(int, sys.stdin.readline().strip().split(" ")))
maze = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for c in line:
        tmp.append(int(c))
    maze.append(tmp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))
while q:
    curr = q.popleft()
    for i in range(4):
        next_x = curr[0] + dx[i]
        next_y = curr[1] + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m \
                and maze[next_x][next_y] == 1:
            maze[next_x][next_y] = maze[curr[0]][curr[1]] + 1
            q.append((next_x, next_y))

print(maze[n-1][m-1])
