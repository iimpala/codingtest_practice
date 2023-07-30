# heap
import sys
import heapq

n, l = tuple(map(int, sys.stdin.readline().strip().split(" ")))
a = list(map(int, sys.stdin.readline().strip().split(" ")))

d = []
h = []

for i in range(n):
    heapq.heappush(h, (a[i], i))

    while h[0][1] < i - l + 1:
        heapq.heappop(h)

    d.append(h[0][0])

for i in d:
    print(i, end=" ")


# deque
# import sys
# from collections import deque
#
# n, l = tuple(map(int, sys.stdin.readline().strip().split(" ")))
# a = list(map(int, sys.stdin.readline().strip().split(" ")))
#
# d = [a[0]]
# q = deque([(a[0], 0)])
#
# for i in range(1, n):
#     if a[i] <= q[0][0]:
#         q.appendleft((a[i], i))
#     else:
#         while a[i] < q[-1][0]:
#             q.pop()
#         q.append((a[i], i))
#
#     while i - l + 1 > q[0][1]:
#         q.popleft()
#
#     d.append(q[0][0])
#
# for i in d:
#     print(i, end=" ")
