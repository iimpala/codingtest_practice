import sys

n = int(sys.stdin.readline().strip())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().strip())

cnt = 0
stack = []
for word in words:
    stack.clear()
    for c in word:
        if stack:
            if stack[-1] == 'A' and c == 'A':
                stack.pop()
            elif stack[-1] == 'B' and c == 'B':
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    if not stack:
        cnt += 1

print(cnt)
