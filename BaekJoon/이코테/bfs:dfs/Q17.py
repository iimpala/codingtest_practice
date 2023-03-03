# 경쟁적 전염
import sys
from copy import deepcopy

def bfs(graph, virus):
    d = [(0,1), (1,0), (-1,0), (0,-1)]
    tmp = deepcopy(virus)
    for i, v in enumerate(tmp):
        for x,y in v:
            for dx, dy in d:
                if x+dx >= 0 and x+dx < N and y+dy >= 0 and y+dy < N and graph[x+dx][y+dy] == 0:
                    graph[x+dx][y+dy] = i
                    virus[i].append((x+dx, y+dy))

N, K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
S, X, Y = map(int, sys.stdin.readline().split())

virus = [[] for _ in range(K+1)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus[graph[i][j]].append((i,j))

for sec in range(S):
    bfs(graph, virus)
    if graph[X-1][Y-1] != 0:
        break

print(graph[X-1][Y-1])
