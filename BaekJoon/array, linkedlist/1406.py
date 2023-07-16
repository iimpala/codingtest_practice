import sys

str1 = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
str2 = []

for _ in range(n):
    cmd = sys.stdin.readline().strip().split(" ")
    if cmd[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif cmd[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif cmd[0] == 'B':
        if str1:
            str1.pop()
    elif cmd[0] == 'P':
        str1.append(cmd[1])

str1.extend(reversed(str2))
print("".join(str1))

