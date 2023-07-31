import sys

input_str = ""
lines = []
while True:
    input_str = sys.stdin.readline().replace('\n', '')
    if input_str != ".":
        lines.append(input_str)
    else:
        break

stack = []
result = []
for line in lines:
    stack.clear()
    balanced = True
    for c in line:
        if c == "[" or c == "(":
            stack.append(c)
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break

    if stack:
        balanced = False

    if balanced:
        result.append("yes")
    else:
        result.append("no")

for r in result:
    print(r)