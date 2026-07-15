import sys
input = sys.stdin.readline
N = int(input())

from collections import deque
matrix = []
for _ in range(N):
    matrix.append(list(map(str, input().strip())))

# 색약 O
visited = [[False] * N for _ in range(N)]
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
for x in range(N):
    for y in range(N):
        if visited[y][x] == True:
            continue
            
        queue.append((x, y))
        while queue:
            col, row = queue.popleft()
            now = matrix[row][col]
            visited[row][col] = True
            for i in range(4):
                nx, ny = col + dx[i], row + dy[i]
                if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == False:
                    if now != 'B' and matrix[ny][nx] != 'B':
                        visited[ny][nx] = True
                        queue.append((nx, ny))
                    
                    if now == 'B' and matrix[ny][nx] == 'B':
                        visited[ny][nx] = True
                        queue.append((nx, ny))

                    
        cnt += 1        



# 색약 X
visited = [[False] * N for _ in range(N)]
queue = deque()

cnt2 = 0
for x in range(N):
    for y in range(N):
        if visited[y][x] == True:
            continue
            
        queue.append((x, y))
        while queue:
            col, row = queue.popleft()
            now = matrix[row][col]
            visited[row][col] = True
            for i in range(4):
                nx, ny = col + dx[i], row + dy[i]
                if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == False:
                    if now == 'B' and matrix[ny][nx] == 'B':
                        visited[ny][nx] = True
                        queue.append((nx, ny))

                    if now == 'R' and matrix[ny][nx] == 'R':
                        visited[ny][nx] = True
                        queue.append((nx, ny))

                    if now == 'G' and matrix[ny][nx] == 'G':
                        visited[ny][nx] = True
                        queue.append((nx, ny))
         
        cnt2 += 1

# print(visited)
print(cnt2, cnt)