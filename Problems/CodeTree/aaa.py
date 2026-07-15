n, m, r, c = map(int, input().split())

# Please write your code here.
grid = [[0] * n for _ in range(n)]
r -= 1
c -= 1
grid[r][c] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
boom = deque([(r, c)])
cnt = 0
for t in range(1, m+1):
    dist = 2**(t-1)
    size = len(boom)    # 이번 회차에 처리해야 하는 폭탄 수
    new_boom = []

    for _ in range(size):
        y, x = boom.popleft()
        boom.append((y, x))
        for i in range(4):
            ny, nx = y + (dy[i] * dist), x + (dx[i] * dist)
            if 0 <= ny < n and 0 <= nx < n:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = 1
                    new_boom.append((ny, nx))

    for y, x in new_boom:
        boom.append((y, x))

result = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            result += 1

print(result)