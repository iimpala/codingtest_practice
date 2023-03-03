# 연구소
import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

def count_safe(graph):
    cnt = 0
    for row in graph:
        cnt += row.count(0)
    return cnt

def bfs(graph):
    q = deque()
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                q.append((i,j))
    
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph[x]):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

N, M = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N)]
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    graph[i] = line

safe = 0
for walls in combinations([(i, j) for i in range(N) for j in range(M)], 3):
    tmp = deepcopy(graph)
    flag = True
    for wall in walls:
        if tmp[wall[0]][wall[1]] != 0:
            flag = False
            break
        else:
            tmp[wall[0]][wall[1]] = 1
    
    if flag:
        bfs(tmp)
        safe = max(safe, count_safe(tmp))

print(safe)