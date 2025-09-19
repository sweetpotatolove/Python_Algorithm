import sys
input = sys.stdin.readline

T = int(input())
base = [1, 1, 1, 2, 2, 3]
for test_case in range(T):
    N = int(input())

    if N <= 6:
        print(base[N-1])
    else:
        dp = [0] * N
        dp[0:6] = base[:]
        for i in range(6, N):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[N-1])