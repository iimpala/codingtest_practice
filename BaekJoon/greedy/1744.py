import sys

n = int(sys.stdin.readline())
positive = []
negative = []
zero = False
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zero = True

sum = 0
if len(positive) != 0:
    positive.sort(reverse=True)
    i = 0
    while(i < len(positive)):
        if i+1 < len(positive):
            if positive[i] != 1 and positive[i+1] != 1:
                sum += positive[i] * positive[i+1]
                i += 2
            else:
                sum += positive[i]
                i +=1
        else:
            sum += positive[i]
            i += 1


if len(negative) != 0:
    negative.sort()
    i = 0
    while(i < len(negative)):
        if i+1 < len(negative):
            sum += negative[i] * negative[i+1]
            i += 2
        else:
            if not zero:
                sum += negative[i]
                i += 1
            else:
                i += 1

print(sum)

# n = 1; sum = num[0]
# num[i] == 0 or 1; sum += num[i]
# num[i] < 0; 작은 순서로 정렬 and 앞에서부터 두개씩 곱하기
# else -> 큰 순서로 정렬 and 앞에서부터 두개씩 곱하기
