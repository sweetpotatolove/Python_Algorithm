n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# n = row
# m = col
from collections import deque
pick = deque()
ok = False
visited = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            pick.append((i, j, 0))
            ok = True
            visited[i][j] = True
            break
    if ok:
        break

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while pick:
    #print(pick)
    row, col, now = pick.popleft()
    result[row][col] = now
    for d in range(4):
        nr, nc = row + dy[d], col + dx[d]
        if 0 <= nr < n and 0 <= nc < m:
            if grid[nr][nc] == 1 and visited[nr][nc] == False:
                pick.append((nr, nc, now + 1))
                visited[nr][nc] = True

for y in range(n):
    for x in range(m):
        if grid[y][x] == 1 and result[y][x] == 0:
            result[y][x] = -1

for z in range(n):
    print(*result[z])