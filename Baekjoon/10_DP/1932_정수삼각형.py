import sys
input = sys.stdin.readline

n = int(input())
# numbers = [num for _ in range(n) for num in map(int, input().split())]
numbers = [list(map(int, input().split())) for _ in range(n)]

memo = [[0] * i for i in range(1, n+1)]
memo[0][0] = numbers[0][0]
for i in range(1, n):
    for j in range(len(numbers[i])):
        if j == 0:
            memo[i][j] = numbers[i][j] + memo[i-1][0]
        elif j == (len(numbers[i]) - 1):
            memo[i][j] = numbers[i][j] + memo[i-1][j-1]
        else:
            memo[i][j] = numbers[i][j] + max(memo[i-1][j-1], memo[i-1][j])
        

print(max(memo[-1]))
