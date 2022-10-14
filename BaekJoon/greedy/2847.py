import sys

n = int(sys.stdin.readline())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline()))

count = 0
score.reverse()
for i in range(n):
    if i+1 < n and score[i] <= score[i+1]:
        count += score[i+1] - score[i] + 1
        score[i+1] = score[i] - 1

print(count)