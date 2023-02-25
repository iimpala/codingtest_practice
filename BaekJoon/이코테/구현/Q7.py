# 럭키 스트레이트
N = int(input())
num = list(map(int, str(N)))
l = len(num)
left = sum(num[:l//2])
right = sum(num[l//2:])
if left == right:
    print("LUCKY")
else:
    print("READY")
