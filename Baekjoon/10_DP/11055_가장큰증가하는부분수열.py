import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# input = 1 100 2 50 60 3 5 6 7 8
dp = [0] * N

for i in range(N):
    dp[i] = A[i]    # 현재 자리 숫자만 고르는 경우
    for j in range(i):  # 앞 수열들의 합
        if A[j] < A[i]:     # 증가하는 수열 조건에 부합하면
            dp[i] = max(dp[i], dp[j] + A[i])    # 업뎃 해가면서 비교

# dp = [1, 101, 3, 53, 113, 6, 11, 17, 24, 32]
print(max(dp))