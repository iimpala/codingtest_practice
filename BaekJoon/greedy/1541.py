# import sys
# import re
#
# line = sys.stdin.readline().strip()
#
# num = re.split('[+-]', line)
# operation = []
# for s in re.split('[0123456789]', line):
#     if s != '':
#         operation.append(s)
# operation.insert(0, '$')
#
# result = 0
# temp = 0
#
# for n, op in reversed(list(zip(map(int,num), operation))):
#     temp += n
#     if op == '$':
#         result += temp
#     elif op == '-':
#         result -= temp
#         temp = 0
#
# print(result)


line = input().split('-')
num = []
for expr in line:
    temp = 0
    plus = expr.split('+')
    for n in plus:
        temp += int(n)
    num.append(temp)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)
