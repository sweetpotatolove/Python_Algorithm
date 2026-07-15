import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

벽후보 = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            벽후보.append((i, j))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_safe = 0

for wall in combinations(벽후보, 3):
    temp = [x[:] for x in board]
    for x, y in wall:
        temp[x][y] = 1  # 벽세우기
    
    
    queue = deque() # 바이러스
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                queue.append((i, j))    # 바이러스 위치

    # 바이러스 퍼뜨리기
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))
    
    # 안전 영역 카운트
    safe = 0
    for row in temp:
        for r in row:
            if r == 0:
                safe += 1

    max_safe = max(max_safe, safe)
    
print(max_safe)