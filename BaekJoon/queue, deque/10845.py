import sys
from collections import deque

n = int(sys.stdin.readline().strip())

cmd = []

for _ in range(n):
    cmd.append(tuple(sys.stdin.readline().strip().split()))

q = deque()
result = []
for c in cmd:
    op = c[0]
    if op == 'push':
        q.append(int(c[1]))
    elif op == 'pop':
        if q:
            result.append(q.popleft())
        else:
            result.append(-1)
    elif op == 'size':
        result.append(len(q))
    elif op == 'empty':
        if q:
            result.append(0)
        else:
            result.append(1)
    elif op == 'front':
        if q:
            result.append(q[0])
        else:
            result.append(-1)
    elif op == 'back':
        if q:
            result.append(q[-1])
        else:
            result.append(-1)

for r in result:
    print(r)
