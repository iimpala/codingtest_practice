import sys
from collections import deque
from copy import deepcopy

def bfs(maze, q):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))

n, m = map(int, sys.stdin.readline().strip().split(" "))

maze = []
pos = deque()
fire = deque()
for i in range(n):
    line = sys.stdin.readline().strip()
    tmp = []
    for j in range(m):
        if line[j] == "#":
            tmp.append(-1)
        elif line[j] == "F":
            tmp.append(0)
            fire.append((i, j))
        elif line[j] == ".":
            tmp.append(0)
        elif line[j] == "J":
            tmp.append(0)
            pos.append((i, j))
    maze.append(tmp)

fire_maze = deepcopy(maze)
pos_maze = deepcopy(maze)

for i, j in fire:
    fire_maze[i][j] = 1
bfs(fire_maze, fire)

pos_maze[pos[0][0]][pos[0][1]] = 1
bfs(pos_maze, pos)

result = []
for i in range(n):
    for j in range(m):
        if (i == 0 or i == n-1 or j == 0 or j == m-1) \
                and maze[i][j] == 0 \
                and pos_maze[i][j] > 0:
            if fire_maze[i][j] == 0 or fire_maze[i][j] > pos_maze[i][j]:
                result.append(pos_maze[i][j])

if not result:
    print("IMPOSSIBLE")
else:
    print(min(result))

