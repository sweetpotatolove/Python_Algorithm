import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
start = end = 0
current_sum = 0

while True:
    if current_sum >= M:
        if current_sum == M:
            cnt += 1
        # 줄이기
        current_sum -= A[start]
        start += 1
    elif end == len(A):
        break
    else:
        # 늘리기
        current_sum += A[end]
        end += 1

print(cnt)
