# 문자열 재정렬
String = "AJKDLSI412K4JSJ9D"
sum = 0
result = ''

for s in String:
    if '0' <= s and s <= '9':
        sum += int(s)
    else:
        result += s
result = sorted(result)
print(''.join(result) + str(sum))