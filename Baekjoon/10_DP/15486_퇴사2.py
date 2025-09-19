import sys
input = sys.stdin.readline
N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N+1)
for j in range(N):
    if j + T[j] <= N:
        # 날짜 기준
        dp[j + T[j]] = max(dp[j] + P[j], dp[j + T[j]])
        # print(dp)
    # 일 안했을 때 기록 안해두면 최대 수익이 다음날로 안이어지는 경우 생김
    dp[j+1] = max(dp[j+1], dp[j])

print(max(dp))