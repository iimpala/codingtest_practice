import sys

expr = sys.stdin.readline().strip().replace("[]", "3").replace("()", "2")

stack = []
is_valid = True
for c in expr:
    if not is_valid:
        break

    if c == ")":
        if not stack:
            is_valid = False
            break

        tmp = 0
        while stack[-1] != "(":
            t = stack.pop()
            if t == "[":
                is_valid = False
                break
            else:
                tmp += int(t)

            if not stack:
                is_valid = False
                break

        if is_valid:
            stack.pop()
        stack.append(2 * tmp)

    elif c == "]":
        if not stack:
            is_valid = False
            break

        tmp = 0
        while stack[-1] != "[":
            t = stack.pop()

            if t == "(":
                is_valid = False
                break
            else:
                tmp += int(t)

            if not stack:
                is_valid = False
                break

        if is_valid:
            stack.pop()
        stack.append(3 * tmp)

    else:
        stack.append(c)

if "[" in stack or "(" in stack:
    is_valid = False

if is_valid:
    print(sum(map(int, stack)))
else:
    print(0)
