import sys

n = int(sys.stdin.readline())
building = []
for _ in range(n):
    building.append(int(sys.stdin.readline()))

stack = [(1000000001, -1)]
cnt = 0

for i in range(n-1, -1, -1):
    tmp = 0
    while stack[-1][0] < building[i]:
        tmp += stack[-1][1] + 1
        stack.pop()
    stack.append((building[i], tmp))
    cnt += tmp

print(cnt)
