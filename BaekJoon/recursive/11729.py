import sys

n = int(sys.stdin.readline().strip())
mv = {
    (1, 2): [(1, 3), (1, 2), (3, 2)],
    (1, 3): [(1, 2), (1, 3), (2, 3)],
    (2, 1): [(2, 3), (2, 1), (3, 1)],
    (2, 3): [(2, 1), (2, 3), (1, 3)],
    (3, 1): [(3, 2), (3, 1), (2, 1)],
    (3, 2): [(3, 1), (3, 2), (1, 2)]
}

def hanoi(n, move):
    if n == 1:
        return [move]
    elif n == 2:
        return mv[move]

    return hanoi(n - 1, mv[move][0]) + [move] + hanoi(n - 1, mv[move][2])

result = hanoi(n, (1, 3))

print(len(result))
for m in result:
    print(m[0], m[1])