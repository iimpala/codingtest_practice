import sys

n = int(sys.stdin.readline())

line = []

for _ in range(n):
    line.append(int(sys.stdin.readline()))

stack = []
cnt = 0
for i in range(n):
    same = 1
    tmp = 0
    if stack:
        if stack[-1][0] > line[i]:
            tmp = 1
        else:
            while stack and stack[-1][0] <= line[i]:
                s = stack.pop()
                tmp += s[1]

                if s[0] == line[i]:
                    same += s[1]

            if stack:
                tmp += 1

    cnt += tmp
    stack.append((line[i], same))

print(cnt)
