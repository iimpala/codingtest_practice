import sys
from collections import deque


m, n, h = map(int, sys.stdin.readline().strip().split(" "))
box = [[] for _ in range(h)]

for k in range(h):
    for _ in range(n):
        box[k].append(list(map(int, sys.stdin.readline().strip().split(" "))))

cnt = 0
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                cnt += 1
            elif box[i][j][k] == 1:
                q.append((i, j, k))

dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]

max_day = 1
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h \
                and box[nz][nx][ny] == 0:
            cnt -= 1
            box[nz][nx][ny] = box[z][x][y] + 1
            q.append((nz, nx, ny))
            max_day = max(max_day, box[nz][nx][ny])

if cnt > 0:
    print(-1)
else:
    print(max_day - 1)
