import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * n

# dp[2] = 2 * dp[0] + dp[1]
if n == 1:
    print(1 % 10007)
else:
    dp[0] = 1
    dp[1] = 3
    
    for i in range(2, n):
        dp[i] = 2 * dp[i-2] + dp[i-1]

    print(dp[n-1] % 10007)