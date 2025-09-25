import sys
input = sys.stdin.readline
N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]
flowers.sort()
# print(flowers)

# 3 1 ~ 11 30
current = (3, 1)    # 시작
end = (11, 30)

i = 0
long_period = (0, 0)
cnt = 0
for _ in range(N):
    update = False
    # 현재 날짜 이전에 피는 꽃인지 확인하고 가장 늦게 지는 꽃 찾기
    while i < N and ((flowers[i][0], flowers[i][1]) <= current) :
        if (flowers[i][2], flowers[i][3]) > long_period:
            long_period = (flowers[i][2], flowers[i][3])
            update = True   # 한번이라도 갱신됐으면 true
        i += 1
    
    # 꽃 선택했으면 
    if update:
        current = long_period   # 현재 날짜 갱신
        cnt += 1
        if current > end:   # 만약 11월30일 지났으면 끝
            break

    else:   # 11월 30일 안됐는데 꽃 선택 못했으면
        cnt = 0
        break

# 마지막꽃이 11월30일까지 펴있었는지 확인
if current <= end:
    cnt = 0

print(cnt)
