# 모험가 길드
fear = [1,1,1,1,1]
fear.sort()
ans = 0     # 그룹 수
cnt = 0     # 그룹 별 멤버 수

for i in fear:
    cnt += 1        # 그룹에 사람 추가
    if cnt >= i:    # 사람수가 공포도 이상이면 출발
        ans += 1    # 그룹 결성
        cnt = 0     # 그룹 초기화
print(ans)
