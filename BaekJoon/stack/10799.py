import sys

line = sys.stdin.readline().strip().replace("()", "|")

cnt = 0
stack = []
for c in line:
    if c == "(":
        stack.append(c)
    elif c == ")":
        stack.pop()
        cnt += 1
    elif c == "|":
        cnt += len(stack)

print(cnt)
