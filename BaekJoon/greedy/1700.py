import sys
import heapq

n, k = map(int, sys.stdin.readline().strip().split(" "))
schedule = list(map(int, sys.stdin.readline().strip().split(" ")))

position = dict([])
plug = [False for _ in range(101)]
plugged = 0

for i, s in enumerate(schedule):
    if str(s) not in position.keys():
        position[str(s)] = []
    position[str(s)].append(i)

for k in position.keys():
    position[k].append(101)

hq = []

cnt = 0
for s in schedule:
    if not plug[s]:
        if plugged < n:
            plug[s] = True
            plugged += 1
        else:
            cnt += 1
            r, i = heapq.heappop(hq)
            plug[i] = False
            plug[s] = True
    else:
        hq.remove((-position[str(s)][0], s))

    position[str(s)].pop(0)
    heapq.heappush(hq, (-position[str(s)][0], s))

print(cnt)
