import sys
input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

positive = []
negative = []

ones_cnt = 0
zeros_cnt = 0
for num in numbers:
    if num > 1:
        positive.append(num)
    elif num == 1:
        ones_cnt += 1
    elif num == 0:
        zeros_cnt += 1
    else:
        negative.append(num)

positive.sort()
negative.sort()

result = ones_cnt
for i in range(len(positive) - 1, 0, -2):
    result += (positive[i] * positive[i-1])

if len(positive) % 2 == 1:
    result += positive[0]

for j in range(0, len(negative) -1, 2):
    result += (negative[j] * negative[j+1])

if len(negative) % 2 == 1 and zeros_cnt == 0:
    result += negative[-1]

print(result)
