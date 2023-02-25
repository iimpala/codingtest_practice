import sys
import heapq

m, n = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
# num.sort()

# for i in range(n):
#     num[0] = num[1] = num[0] + num[1]
#     num.sort()

# print(sum(num))

heapq.heapify(num)

for i in range(n):
    merge = heapq.heappop(num) + heapq.heappop(num)
    heapq.heappush(num, merge)
    heapq.heappush(num, merge)

print(sum(num))