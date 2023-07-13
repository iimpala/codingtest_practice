import sys
import heapq

n = int(sys.stdin.readline())

month_start = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
schedules = []
for _ in range(n):
    sm, sd, em, ed = tuple(map(int, sys.stdin.readline().strip().split(' ')))
    s = month_start[sm-1] + (sd-1)
    e = month_start[em-1] + (ed-1)
    schedules.append((s, e))

schedules.sort(key=lambda x: (x[0], x[1]))
hq = []
now = 60

result = 0

for i in range(n):
    start, end = schedules[i]

    if start <= now:
        heapq.heappush(hq, -end)
    else:
        if len(hq) == 0:
            result = 0
            break
        else:
            now = -(heapq.heappop(hq))
            result += 1
            hq.clear()
            if start <= now:
                heapq.heappush(hq, -end)
            else:
                result = 0
                break

    if now > 334:
        break

if now <= 334 and len(hq) > 0:
    if -hq[0] > 334:
        result += 1
    else:
        result = 0

print(result)
