import sys
input = sys.stdin.readline
N = int(input())
P = sorted(list(map(int, input().split())))

total = 0
for i in range(N+1):
    time = 0
    for j in range(i):
        time += P[j]
    total += time

print(total)