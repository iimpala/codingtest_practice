import sys
from collections import deque


n, m = tuple(map(int, sys.stdin.readline().strip().split(" ")))
pos = list(map(int, sys.stdin.readline().strip().split(" ")))

q = deque()
for _ in range(n):
    q.append(False)

for i in pos:
    q[i-1] = i

cnt = 0

for i in pos:
    idx = q.index(i)
    left = idx
    right = len(q) - left

    if left <= right:
        cnt += left
        for _ in range(left):
            q.append(q.popleft())
    else:
        cnt += right
        for _ in range(right):
            q.appendleft(q.pop())
    q.popleft()

print(cnt)
