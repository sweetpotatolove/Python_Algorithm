import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
box = []
for _ in range(H):
    box_temp = []
    for _ in range(N):
        box_temp.append(list(map(int, input().strip().split())))
    box.append(box_temp)

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((x, y, z))

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nx, ny, nz))

ok = False
result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                ok = True
                break
            
            result = max(result, box[z][y][x])

        if ok:
            break
    if ok:
        break
if ok:
    print(-1)
else:
    print(result -1)
