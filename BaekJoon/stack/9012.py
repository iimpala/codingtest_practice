import sys

n = int(sys.stdin.readline().strip())

ps = []
for _ in range(n):
    ps.append(sys.stdin.readline().strip())

result = []
stack = []

for s in ps:
    stack.clear()
    is_valid = True
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False

    if is_valid:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)
