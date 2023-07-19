import sys

n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().strip().split(" ")))
height.insert(0, 100000001)

stack = [(0, height[0])]
result = []
for i in range(1, n+1):
    while stack[-1][1] < height[i]:
        stack.pop()

    result.append(stack[-1][0])
    stack.append((i, height[i]))

for i in result:
    print(i, end=" ")
