import sys

s = sys.stdin.readline().strip()
bar = 0

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        continue
    else:
        bar += 1

print((bar+1) // 2)