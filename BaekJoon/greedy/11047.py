import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

count = 0
curr = 0
for coin in coins:
    if curr + coin > k:
        continue
    else:
        count += ((k-curr) // coin)
        curr += coin * ((k-curr) // coin)
        
print(count)