import sys

n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

stack = [0]
cmd = []
current = 0
flag = True
for i in num_list:
    if stack[-1] > i:
        flag = False
        break

    while stack[-1] < i:
        current += 1
        stack.append(current)
        cmd.append('+')
    stack.pop()
    cmd.append('-')

if flag:
    for p in cmd:
        print(p)
else:
    print("NO")
