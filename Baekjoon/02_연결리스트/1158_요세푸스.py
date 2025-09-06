import sys
input = sys.stdin.readline
N, K = map(int, input().split())

people = []
for i in range(1, N+1):
    people.append(i)

result = []
idx = 0
while people:
    idx = (idx + K - 1) % len(people)
    result.append(people.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')
    