import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    dp[i] += 1  # 자기 자신 일단 넣고
    for j in range(i):
        if A[j] < A[i]: # 나보다 작은애 찾으면
            dp[i] = max(dp[i], dp[j] + 1)   # 업뎃 해가면서 비교

print(max(dp))