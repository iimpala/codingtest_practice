# 만들 수 없는 금액
coin = [13,3,1,5,1,1]
coin.sort()

target = 1
for i in coin:
    if i <= target:
        target += i
    else: 
        break
    
print(target)
