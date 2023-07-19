import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split(" ")))

MAX_VAL = 1000001
nge = []
stack = [MAX_VAL]

for i in range(n-1, -1, -1):
    while stack[-1] <= a[i]:
        stack.pop()

    if stack[-1] == MAX_VAL:
        nge.append(-1)
    else:
        nge.append(stack[-1])

    stack.append(a[i])

for i in reversed(nge):
    print(i, end=" ")

