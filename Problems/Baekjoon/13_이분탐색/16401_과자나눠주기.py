import sys
input = sys.stdin.readline
M, N = map(int, input().split())
snack = list(map(int, input().split()))

start = 1
end = max(snack)
result = 0

# 1부터 과자의 최대 크기만큼 반복
while start <= end:
    mid = (start + end) // 2    # 중간부터
    cnt = 0
    for s in snack:
        cnt += (s // mid)  # 과자들을 중간 길이로 나눠 생기는 조각 수 더하기
    
    if cnt >= M:    # 나눠줄 수 있으면
        result = mid    # 가능한 길이 저장
        start = mid + 1     # 더 긴 길이 시도
    else:
        end = mid - 1   # 조각 수 부족해서 나눠줄 수 없으면
                        # 길이 줄여야함

print(result)

