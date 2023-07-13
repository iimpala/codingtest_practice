import sys
import heapq

n = int(sys.stdin.readline())

schedules = []
for i in range(n):
    s = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    schedules.append(s)

schedules.sort()

hq = []

heapq.heappush(hq, schedules[0][1])
for i in range(1, n):
    heapq.heappush(hq, schedules[i][1])
    if hq[0] <= schedules[i][0]:
        heapq.heappop(hq)

print(len(hq))
