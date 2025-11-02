import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
    # 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque
robot = deque()
robot.append((r, c, d))

cnt = 0
while robot:
    row, col, d = robot.popleft()

    # 현재 칸 청소 전이면, 현재 칸 청소
    if room[row][col] == 0:
        room[row][col] = 2 # 청소 완 표시
        cnt += 1
    
    ok = False
    # 주변 4칸 살펴보기
    for i in range(4):
        d = (d + 3) % 4     # 반시계방향
        nrow, ncol = row + dy[d], col + dx[d]
        # 청소안된 빈칸 있는 경우
        if 0 <= nrow < N and 0 <= ncol < M and room[nrow][ncol] == 0:
            robot.append((nrow, ncol, d))
            ok = True
            break
    
    # 청소 안된 빈칸 없는 경우
    if ok == False:
        nrow, ncol = row - dy[d], col - dx[d]   # 후진
        if room[nrow][ncol] == 1:
            break
        robot.append((nrow, ncol, d))

print(cnt)
