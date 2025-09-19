import sys
input = sys.stdin.readline
N = int(input())

dp = [[0] * 10 for _ in range(N)]
    #    0  1  2  3  4  5  6  7  8  9
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # -> 첫째자리
      #    0  1  2  3  4  5  6  7  8  9
# dp[1] = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1] -> 둘째자리
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1]) % 1000000000)