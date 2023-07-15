import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().strip().split(" ")))

# Greedy
# pos = [0 for _ in range(n+1)]
# for i in range(n):
#     pos[line[i]] = i
#
# max_count = 0
# for i in range(n):
#     current = line[i]
#     count = 1
#
#     while current + 1 <= n and pos[current] < pos[current + 1]:
#         count += 1
#         current += 1
#
#     max_count = max(max_count, count)


# Dp
lis = [0 for _ in range(n+1)]

for i in range(n):
    current = line[i]
    lis[current] = lis[current-1] + 1

max_count = max(lis)

print(n - max_count)
