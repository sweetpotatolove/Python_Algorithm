import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    dp[i] = A[i]
    
    if i == 0:
        continue

    dp[i] = max(dp[i], dp[i-1] + A[i])

    
print(max(dp))


