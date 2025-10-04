import sys
input = sys.stdin.readline
N = int(input())
cards = set(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    if i in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
