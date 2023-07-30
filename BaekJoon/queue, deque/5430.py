import sys
from collections import deque

n = int(sys.stdin.readline().strip())

cmd = []
arrays = []

for _ in range(n):
    cmd.append(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    if m > 0:
        arr = sys.stdin.readline().strip().replace("[", "").replace("]", "").split(",")
        arrays.append(deque(map(int, arr)))
    else:
        arr = sys.stdin.readline()
        arrays.append(deque())

result = []
for i in range(n):
    rev = False
    err = False

    for c in cmd[i]:
        if c == 'R':
            rev = not rev
        elif c == 'D':
            if len(arrays[i]) == 0:
                err = True
                break
            if rev:
                arrays[i].pop()
            else:
                arrays[i].popleft()

    if err:
        result.append('error')
    else:
        if rev:
            arr = list(map(str, reversed(arrays[i])))
        else:
            arr = list(map(str, arrays[i]))

        result.append(f"[{','.join(arr)}]")

for r in result:
    print(r)
