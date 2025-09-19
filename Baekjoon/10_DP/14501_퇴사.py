import sys
input = sys.stdin.readline
N = int(input())
T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * N
for j in range(N):
    if j + T[j] <= N:
        dp[j] = P[j]
        for k in range(j):
            if k + T[k] <= j:
                dp[j] = max(dp[j], dp[k] + P[j])
            # print(dp)

print(max(dp))


