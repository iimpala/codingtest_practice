import sys

vilages, storage = sys.stdin.readline().split()
vilages = int(vilages)
storage = int(storage)

n = int(sys.stdin.readline())
info = []

for i in range(n):
    src, dest, box = sys.stdin.readline().split()
    info.append((int(src), int(dest), int(box)))

info.sort(key=lambda x: (x[1]-x[0], x[1]))
delivered = 0
truck = [0] * (vilages+1)
full = -1
weight = 0

for deliver in info:
    if deliver[0] <= full:
        continue

    if storage in truck[deliver[0]:deliver[1]]:
        full = deliver[0] + truck[deliver[0]:deliver[1]].index(storage)
        continue

    else:
        weight = deliver[2]
        m = max(truck[deliver[0]:deliver[1]])
        if m + deliver[2] > storage:
            weight = storage - m

        delivered += weight
        for i in range(deliver[0], deliver[1]):
            truck[i] += weight

print(delivered)

"""
    <답>
    배달정보를 [도착지가 가까운 순서] 로 정렬
    -> 정렬된 배달정보를 순회하면서 [각 도시별 트럭의 상태]를 업데이트
    -> 한 도시에서 트럭이 가득 찼으면 그 도시를 지나가는 배달은 고려하지 않음

    <풀이과정>
    1. 출발지가 가까운순으로 정렬 -> lookup table생각x, 구현 못함
    2. 각 도시를 노드, 배달하는 짐의 양을 간선의 가중치로 놓고 그래프 구성 -> 1번 맞음, 2번 틀림(배달하지 않아야하는 짐을 걸러내지 못함)
    3. 출발지와 도착지 사이의 거리가 가까운순으로 정렬, 각 도시에서 트럭에 실려있는 무게를 기록 
        -> 테스트케이스 정답, 시간부족(순서가 섞여있어 full인덱스가 늦게 반영되어 많은 케이스를 걸러내지 못한것 같음)
    4. 도착지가 가까운순으로 정렬 -> 정답(full 인덱스가 많은 케이스를 걸러내어 제한시간안데 들어온 것으로 추정)

    <소요시간>
    188ms(PyPy3)
    1108ms(Python3)
"""


# 64ms(Python3) 답
# import sys
# input = sys.stdin.readline
# n, c = map(int, input().split())
# m = int(input())
# infos = [list(map(int, input().split())) for _ in range(m)]
# infos.sort(key=lambda x:[x[0], x[1]])
# cur = 1
# ans = 0
# capacity = [0] * (n+1)
# all = c
# for info in infos:
#     if cur != info[0]:
#         cur = info[0]
#         all += capacity[cur]
#         ans += capacity[cur]
#         capacity[cur] = 0
#     if all >= info[2]:
#         capacity[info[1]] += info[2]
#         all -= info[2]
#     else:
#         capacity[info[1]] += all
#         all = 0
# print(ans + sum(capacity))