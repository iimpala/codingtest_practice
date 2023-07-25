import sys

histogram = []
while True:
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    n = line.pop(0)
    if n == 0:
        break
    else:
        histogram.append(line)

result = []
for hist in histogram:
    stack = [[0, 0]]
    max_area = 0

    for h in hist:
        if stack[-1][0] < h:
            stack.append([h, 1])
        elif stack[-1][0] == h:
            stack[-1][1] += 1
        else:
            tmp_w = 0
            tmp_a = []
            while stack[-1][0] > h:
                s = stack.pop()
                tmp_w += s[1]
                tmp_a.append(s[0] * tmp_w)

            if stack[-1][0] < h:
                stack.append([h, tmp_w + 1])
            elif stack[-1][0] == h:
                stack[-1][1] += tmp_w + 1

            max_area = max(max_area, max(tmp_a))

    tmp_w = 0
    tmp_a = []
    while stack:
        s = stack.pop()
        tmp_w += s[1]
        tmp_a.append(s[0] * tmp_w)
    max_area = max(max_area, max(tmp_a))

    result.append(max_area)

for r in result:
    print(r)

