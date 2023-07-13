import sys

n = int(sys.stdin.readline())

schedule = []
for i in range(n):
    s, e = map(int, sys.stdin.readline().strip().split(' '))
    schedule.append((s, e))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 0
now = 0

for time in schedule:
    start, end = time
    if start >= now:
        count += 1
        now = end

print(count)
