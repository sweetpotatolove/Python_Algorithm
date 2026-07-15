N, M = map(int, input().split())
puzzles = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
import itertools

result = []
for r in range(1, N + 1):
    for comb in itertools.combinations(puzzles, r):

        cnt = 0
        numbers = set()
        for c in comb:
            numbers.update(c)
            cnt += 1
        if len(numbers) == 10:
            result.append(cnt)
            break

print(min(result))