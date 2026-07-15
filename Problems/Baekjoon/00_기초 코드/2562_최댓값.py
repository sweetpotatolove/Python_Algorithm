import sys
input = sys.stdin.readline
numbers = []
for _ in range(9):
    numbers.append(int(input()))

maxnum = 0
maxindex = 0
for i in range(9):
    if maxnum < numbers[i]:
        maxnum = numbers[i]
        maxindex = i + 1

print(maxnum)
print(maxindex)