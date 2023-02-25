# 문자열 뒤집기
S = "10101010101010010"

cnt= [0, 0]
prev = int(S[0])
cnt[prev] += 1
for i in range(1, len(S)):
    now = int(S[i])
    if prev == 1 and now == 0:
        cnt[0] += 1
    elif prev == 0 and now == 1:
        cnt[1] += 1
    prev = now
print(min(cnt[0],cnt[1]))