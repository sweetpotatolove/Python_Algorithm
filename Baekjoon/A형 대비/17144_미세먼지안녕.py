import sys  
input = sys.stdin.readline
from collections import deque

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

air_r = []
air_c = 0
dust = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            air_r.append(i)
            air_c = j

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

cnt = 0
# 공기 순환지점 찾기
d1, d2 = 0, 0   # 일단 오른쪽부터
y1, x1 = air_r[0] + dy[d1], air_c + dx[d1]
if 0 > y1 or y1 >= R or 0 > x1 or x1 >= C:  # 범위 벗어나면
    d1 = (d1 + 1) % 4   # 방향 바꾸고
    y1, x1 = air_r[0] + dy[d1], air_c + dx[d1]  # 위 방향으로

y2, x2 = air_r[1] + dy[d2], air_c + dx[d2]
if 0 > y2 or y2 >= R or 0 > x2 or x2 >= C:  # 범위 벗어나면
    d2 = (d2 + 3) % 4   # 방향 바꾸고
    y2, x2 = air_r[1] + dy[d2], air_c + dx[d2]  # 아래 방향으로

start_x1, start_y1, start_x2, start_y2 = x1, y1, x2, y2
start_d1, start_d2 = d1, d2
while cnt < T:
    # 공기청정기 윗부분
    while not (y1 == air_r[0] and x1 == air_c):
        if board[y1][x1] != 0 and board[y1][x1] != -1:  # 먼지 있으면
            tempC = 0
            for d in range(4):  # 먼지 날려
                tempY, tempX = y1 + dy[d], x1 + dx[d]
                if 0 <= tempY < R and 0 <= tempX < C and board[tempY][tempX] != -1:
                    # 먼지가 갈 수 있으면 계산
                    tempC += 1
                    board[tempY][tempX] += int(board[y1][x1] / 5)
            board[y1][x1] -= (int(board[y1][x1] / 5) * tempC)
        # 다음 위치
        ny1, nx1 = y1 + dy[d1], x1 + dx[d1]
        if 0 <= ny1 <= air_r[0] and 0 <= nx1 < C:  
            y1, x1 = ny1, nx1
        else:   # 벗어나면 방향 바꿔
            d1 = (d1 + 1) % 4 
            y1, x1 = y1 + dy[d1], x1 + dx[d1]
    

    # 공기청정기 아래부분
    while not (y2 == air_r[1] and x2 == air_c):
        if board[y2][x2] != 0 and board[y2][x2] != -1:  # 먼지 있으면
            tempC = 0
            for d in range(4):  # 먼지 날려
                tempY, tempX = y2 + dy[d], x2 + dx[d]
                if 0 <= tempY < R and 0 <= tempX < C and board[tempY][tempX] != -1:
                    # 먼지가 갈 수 있으면 계산
                    tempC += 1
                    board[tempY][tempX] += int(board[y2][x2] / 5)
            board[y2][x2] -= (int(board[y2][x2] / 5) * tempC)
        # 다음 위치
        ny2, nx2 = y2 + dy[d2], x2 + dx[d2]
        if air_r[1] <= ny2 < R  and 0 <= nx2 < C:  
            y2, x2 = ny2, nx2
        else:   # 벗어나면 방향 바꿔
            d2 = (d2 + 3) % 4 
            y2, x2 = y2 + dy[d2], x2 + dx[d2]
    
    cnt += 1
    y1, x1, y2, x2 = start_y1, start_x1, start_y2, start_x2
    d2, d1 = start_d2, start_d1

result = 0
for i in range(R):
    result += sum(board[i])

print(result + 2)   # 공기청정기 -1이니까 +2해서?







