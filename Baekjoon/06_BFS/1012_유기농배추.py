import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(col, row):
    queue = deque()
    queue.append((col, row))
    matrix[row][col] = 0

    while queue:
        col, row = queue.popleft()
        for i in range(4):
            nx, ny = col + dx[i], row + dy[i]
            if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1:
                queue.append((nx, ny))
                matrix[ny][nx] = 0


T = int(input())

for test_case in range(T):
    M, N, K = map(int, input().split())
    cabbage = []
    for _ in range(K):
        cabbage.append(tuple(map(int, input().split())))

    matrix = [[0] * M for _ in range(N)]
    
    for i, j in cabbage:
        matrix[j][i] = 1
    
    cnt = 0
    for i, j in cabbage:
        # print(matrix)
        if matrix[j][i] == 1:
            bfs(i, j)
            cnt += 1

    print(cnt)