n = int(input())
mountains_str = input().split()
mountains = list(map(int, mountains_str))
height = mountains[0]
opt = 0
kill = 0
for i in range(1, n):
    if height >= mountains[i]:
        kill += 1
        if opt < kill:
            opt = kill
    else:
        kill = 0
        height = mountains[i]

print(opt)