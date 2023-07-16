import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip().split(" ")))
x = int(sys.stdin.readline())

pos = [0 for _ in range(1000001)]
for i, k in enumerate(num):
    pos[k] = i

cnt = 0
for k in num:
    if x - k <= 1000000 and pos[k] < pos[x-k]:
        cnt += 1

print(cnt)
