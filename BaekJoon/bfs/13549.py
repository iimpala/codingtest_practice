import sys
from collections import deque

def mult2(visited, curr):
    q = deque()
    tmp = []

    q.append(curr)
    while q:
        curr = q.popleft()

        next = curr * 2
        if next <= 100000 and not visited[next]:
            line[next] = line[curr]
            visited[next] = True
            q.append(next)
            tmp.append(next)

    return tmp

def bfs(n, k):
    visited = [False for _ in range(100001)]
    q = deque()
    q.append(n)

    while q:
        curr = q.popleft()
        q.extend(mult2(visited, curr))

        if curr == k:
            return line[k]

        for next in [curr - 1, curr + 1]:
            if 0 <= next <= 100000 and not visited[next]:
                line[next] = line[curr] + 1
                q.append(next)
                visited[next] = True

    return line[k]

n, k = map(int, sys.stdin.readline().strip().split(" "))
line = [0 for _ in range(100001)]

print(bfs(n, k))
