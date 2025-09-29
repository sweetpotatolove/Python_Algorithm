import sys
from collections import deque
input = sys.stdin.readline
N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input()) # 뱀 방향 변환 횟수
move = [list(map(str, input().split())) for _ in range(L)]
# [['3', 'D'], ['15', 'L']] -> 3초 뒤 오른쪽 90도, 15초 뒤 왼쪽 90도

board = [[0] * N for _ in range(N)]
for r, c in apple:
    board[r-1][c-1] = 1  # 사과 표시

visited = [[False] * N for _ in range(N)]
visited[0][0] = True   # 뱀 시작위치 1행 1열 고정

#     북 동 남 서 
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]
snake_body = deque()    
snake_body.append((0, 0))

time = 0
d = 1
move_cnt = 0
Hrow, Hcol = 0, 0
while True:
    time += 1
    nx, ny = Hrow + dx[d], Hcol + dy[d]

    # 머리가 갈 수 없는 방향이면 끝
    if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
        break
    
    # 머리 이동
    snake_body.append((nx, ny))
    visited[nx][ny] = True

    # 사과 있으면
    if board[nx][ny] == 1:
        board[nx][ny] = 0   # 사과 먹고
    # 사과 없으면
    else:
        Trow, Tcol = snake_body.popleft()   # 꼬리 좌표
        visited[Trow][Tcol] = False     # 꼬리 칸 비우고

    # 방향 변환
    if move_cnt < len(move):
        if time == int(move[move_cnt][0]): 
            if move[move_cnt][1] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            # 방향전환 했으면 카운트 올리기
            move_cnt += 1

    Hrow, Hcol = nx, ny

print(time)


# 재귀로 풀면 답은 나오는데 뱀이 오랫동안 안죽고 살아있으면
# 재귀 깊이 초과함
'''
def snake(Hrow, Hcol, time, move_cnt, d):
    nx, ny = Hrow + dx[d], Hcol + dy[d]

    # 머리가 갈 수 없는 방향이면 끝
    if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
        return time + 1
    
    # 머리 이동
    snake_body.append((nx, ny))
    visited[nx][ny] = True

    # 사과 있으면
    if board[nx][ny] == 1:
        board[nx][ny] = 0   # 사과 먹고
    # 사과 없으면
    else:
        Trow, Tcol = snake_body.popleft()   # 꼬리 좌표
        visited[Trow][Tcol] = False     # 꼬리 칸 비우고

    # 방향 변환
    if move_cnt < len(move):
        if (time + 1) == int(move[move_cnt][0]): 
            if move[move_cnt][1] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            # 방향전환 했으면 카운트 올리기
            move_cnt += 1

    return snake(nx, ny, time + 1, move_cnt, d)

p = snake(0, 0, 0, 0, 1) # 대가리 위치, 초, 변환횟수, 방향
print(p)
'''