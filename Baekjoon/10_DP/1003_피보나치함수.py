import sys
input = sys.stdin.readline

def fibo(n):
    if n > 1 and (0 in memo[n]):
        for i in range(2):
            memo[n][i] = fibo(n-1)[i] + fibo(n-2)[i]
    return memo[n]

T = int(input())
for test_case in range(T):
    num = int(input())
    memo = [[0, 0] for _ in range(41)] 
    memo[0] = [1, 0]
    memo[1] = [0, 1]
    result = fibo(num)
    for i in range(2):
        print(result[i], end=" ")
    print()


