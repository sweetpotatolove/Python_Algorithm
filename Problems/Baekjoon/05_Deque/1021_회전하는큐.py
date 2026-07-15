import sys
input = sys.stdin.readline
N, M = map(int, input().split())
location = list(map(int, input().strip().split()))
cnt = 0

for i in range(M):
    move = 0
    if location[i] != 1:
        if location[i] - 1 <= N + 1 - location[i]:
            move = location[i] - 1
            for j in range(i+1, M):
                location[j] -= move
                if location[j] < 1:
                    location[j] += N
        else:
            move = N + 1 - location[i]
            for j in range(i+1, M):
                location[j] = (location[j] + move - 1) % N + 1

    N -= 1
    for k in range(i+1, M):
        location[k] -= 1
    
    cnt += move

print(cnt)