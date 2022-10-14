import sys

n = int(sys.stdin.readline())

lines = []
for i in range(n):
    src, dest = sys.stdin.readline().split()
    lines.append((int(src), int(dest)))
lines=sorted(lines, key=lambda x:x[0])

curr = -1000000000
lenth = 0
for line in lines:
    if line[0] >= curr:
        lenth += line[1] - line[0]
        curr = line[1]
    elif line[1] > curr:
        lenth += line[1] - curr
        curr = line[1]
    else:
        continue

print(lenth)