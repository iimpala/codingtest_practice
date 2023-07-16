import sys

n = int(sys.stdin.readline())

pw = []
for _ in range(n):
    line = list(sys.stdin.readline().strip())
    str1 = []
    str2 = []

    for s in line:
        if s == '<':
            if str1:
                str2.append(str1.pop())
        elif s == '>':
            if str2:
                str1.append(str2.pop())
        elif s == '-':
            if str1:
                str1.pop()
        else:
            str1.append(s)
    str1.extend(reversed(str2))
    pw.append(''.join(str1))

for p in pw:
    print(p)
