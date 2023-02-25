# 곱하기 혹은 더하기
S = "02984"

sum = int(S[0])
for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or sum <= 1:
        sum += num
    else:
        sum *= num

print(sum)