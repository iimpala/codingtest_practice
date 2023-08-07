import sys
from collections import deque

def bfs(cube, src, dst):
    dx = [0, 0, 1, 0, 0, -1]
    dy = [0, 1, 0, 0, -1, 0]
    dz = [1, 0, 0, -1, 0, 0]
    q = deque()
    q.append(src)
    cube[src[0]][src[1]][src[2]] = 1

    l = len(cube)
    r = len(cube[0])
    c = len(cube[0][0])
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l and cube[nz][nx][ny] == 0:
                cube[nz][nx][ny] = cube[z][x][y] + 1
                q.append((nz, nx, ny))

    if cube[dst[0]][dst[1]][dst[2]] == 0:
        return "Trapped!"
    else:
        return "Escaped in {} minute(s).".format(cube[dst[0]][dst[1]][dst[2]] - 1)


tc = []
start = []
end = []
l, r, c = map(int, sys.stdin.readline().strip().split(" "))
while (l, r, c) != (0, 0, 0):
    cube = []
    for i in range(l):
        tmp = []
        for j in range(r):
            line = list(sys.stdin.readline().strip())
            for k in range(c):
                if line[k] == "S":
                    start.append((i, j, k))
                    line[k] = 0
                elif line[k] == ".":
                    line[k] = 0
                elif line[k] == "E":
                    end.append((i, j, k))
                    line[k] = 0
                elif line[k] == "#":
                    line[k] = -1
            tmp.append(line)
        sys.stdin.readline()

        cube.append(tmp)
    tc.append(cube)

    l, r, c = map(int, sys.stdin.readline().strip().split(" "))

result = []
for i in range(len(tc)):
    result.append(bfs(tc[i], start[i], end[i]))

for r in result:
    print(r)
