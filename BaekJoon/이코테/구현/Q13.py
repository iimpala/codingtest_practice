# 치킨 배달
import sys
from itertools import combinations

def combList(dist, comb):
    l = []
    for i in comb:
        l.append(dist[i])
    return l

def chickenDist(dist):
    chicken_dist = 0
    for i in range(len(dist[0])):
        chicken_dist += min([d[i] for d in dist])
    return chicken_dist

INF = 10e9
N, M = map(int, sys.stdin.readline().split())
home = []
chicken = []

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if line[j] == 1:
            home.append((i,j))
        elif line[j] == 2:
            chicken.append((i,j))

dist = [[INF for _ in range(len(home))] for _ in range(len(chicken))]
for i, c in enumerate(chicken):
    for j, h in enumerate(home):
        dist[i][j] = abs(c[0] - h[0]) + abs(c[1]-h[1])

chicken_dist = INF
comb = combinations(range(len(chicken)), M)
for c in comb:
    l = combList(dist, c)
    d = chickenDist(l)
    if chicken_dist > d:
        chicken_dist = d
print(chicken_dist)