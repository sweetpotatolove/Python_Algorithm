import sys
import heapq

input = sys.stdin.readline
N = int(input())
hq = []

for _ in range(N):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(hq) < N:
            heapq.heappush(hq, num)
        else:
            if num > hq[0]:
                heapq.heappushpop(hq, num)

print(hq[0])  # N번째 큰 수


''' 메모리 초과
import sys
input = sys.stdin.readline
N = int(input())
result = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in temp:
        result.append(j)

result.sort()
print(result[-N])
'''