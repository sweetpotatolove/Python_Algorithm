import sys  
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
#     북 동 남 서 
dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]
room = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    # 현재 칸 청소 안돼있으면 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소완
        cnt += 1
    
    ok = False
    # 주변 칸 확인(90도)
    for i in range(4):
        d = (d + 3) % 4  # 반시계방향
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            r, c = nx, ny
            ok = True
            break
    
    # 청소할 곳 못찾았으면
    if not ok:  
        bx, by = r - dx[d], c - dy[d]   # 후진
        if room[bx][by] == 1:
            break
        r, c = bx, by

print(cnt)