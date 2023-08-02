import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split(" "))
box = []
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().strip().split(" "))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()

cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
        elif box[i][j] == 0:
            cnt += 1

max_day = 0
while q:
    curr = q.popleft()
    for i in range(4):
        nx = curr[0] + dx[i]
        ny = curr[1] + dy[i]

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            cnt -= 1
            box[nx][ny] = box[curr[0]][curr[1]] + 1
            q.append((nx, ny))
            max_day = max(max_day, box[nx][ny])

if cnt > 0:
    print(-1)
else:
    if max_day > 0:
        print(max_day - 1)
    else:
        print(0)
