import sys
input = sys.stdin.readline

n = int(input())
numbers = [num for _ in range(n) for num in map(int, input().split())]

memo = [[0, 0] for i in range(1, n+1) for _ in range(i)]

print(numbers)
print(memo)