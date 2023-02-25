# 볼링공 고르기
from math import comb

N, M = 8, 5
balls = [1,5,4,3,2,4,5,2]

cnt = [0 for _ in range(M+1)]
for i in balls:
    cnt[i] += 1

result = comb(N,2)
for i in cnt:
    if i >= 2:
        result -= comb(i,2)

print(result)