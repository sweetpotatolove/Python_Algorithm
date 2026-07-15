import heapq
import sys
input = sys.stdin.readline
N = int(input())
hq = []
for i in range(N):
    temp = int(input())
    if temp == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, temp)
