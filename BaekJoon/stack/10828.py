import sys

n = int(sys.stdin.readline())

stack = []
result = []
for _ in range(n):
    cmd = sys.stdin.readline().strip().split(" ")

    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) > 0:
            i = stack.pop()
            result.append(i)
        else:
            result.append(-1)
    elif cmd[0] == 'size':
        result.append(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif cmd[0] == 'top':
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)

for i in result:
    print(i)
