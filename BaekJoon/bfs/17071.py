import sys
from collections import deque


def bfs(visited, n, k):
    q = deque()
    q.append(n)

    if n == k:
        return 0

    t = 0
    while q:
        t += 1
        k += t
        if k > 500000:
            return -1

        for i in range(2):
            if visited[k][i] != 0 and (t - visited[k][i]) % 2 == 0:
                return t

        for _ in range(len(q)):
            curr = q.popleft()

            for next in [curr + 1, curr - 1, curr * 2]:
                if next == k:
                    return t

                if 0 <= next <= 500000:
                    if visited[next][t % 2] == 0:
                        visited[next][t % 2] = t
                        q.append(next)

    return -1


n, k = map(int, sys.stdin.readline().strip().split(" "))
visited = [[0, 0] for _ in range(500001)]

print(bfs(visited, n, k))
