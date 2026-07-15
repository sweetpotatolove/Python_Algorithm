import sys
input = sys.stdin.readline
M, N = map(int, input().split())
u = []
for _ in range(M):
    data = list(map(int, input().split()))
    su = sorted(set(data))
    rank = {v: i for i, v in enumerate(sorted(set(su)))}
    u.append(tuple(rank[x] for x in data))


from collections import Counter
cnt = Counter(u)

result = 0
for c in cnt.values():
    if c >= 2:
        result += c * (c - 1) // 2

print(result)