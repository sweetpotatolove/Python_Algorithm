import sys
input = sys.stdin.readline

dx = [-2, -1, 1, 2,  2,  1, -1, -2]
dy = [-1, -2, -2, -1, 1,  2,  2,  1]

from collections import deque
T = int(input())
for test_case in range(T):
    I = int(input())
    matrix = [[0] * I for _ in range(I)]
    nowX, nowY = map(int, input().split())
    targetX, targetY = map(int, input().split())
    
    queue = deque()
    queue.append((nowX, nowY))
    
    while queue:
        row, col = queue.popleft()
        if row == targetX and col == targetY:
            break
        for i in range(8):
            nx, ny = row + dx[i], col + dy[i]
            if 0 <= nx < I and 0 <= ny < I and matrix[nx][ny] == 0:
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[row][col] + 1
    
    print(matrix[targetX][targetY])
