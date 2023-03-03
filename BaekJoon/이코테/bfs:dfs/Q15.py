# 특정 거리의 도시 찾기
import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
INF = 9999
graph = [[]for _ in range(N+1)]
# for i in range(N):
#     graph[i][i] = 0

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)

dist = [INF for _ in range(N+1)]
visited = [False for _ in range(N+1)]
q = deque()
# 다익스트라는 우선순위큐 -> 방문하지 않은 노드 중 가장 가까운 노드 먼저 탐색 : (dist, 노드번호) 저장, dist가 가장 작은 원소 pop(min heap)

q.append(X)
dist[X] = 0
while q:
    curr = q.popleft()
    visited[curr] = True
    for i in graph[curr]:
        dist[i] = min(dist[i], dist[curr] + 1)
        if visited[i] != True:
            q.append(i)

    # for i in range(N):
    #     if graph[curr][i] != INF:
    #         dist[i] = min(dist[i], dist[curr] + graph[curr][i])
    #         if visited[i] != True:
    #             q.append(i)

if K in dist:
    for i in range(1, N+1):
        if dist[i] == K:
            print(i)
else:
    print(-1)