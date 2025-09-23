import sys
input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

top, bottom, north, south, west, east = 0, 0, 0, 0, 0, 0
m = 0
    # 동, 서, 북, 남
dx = [0, 0, -1, 1]  
dy = [1, -1, 0, 0]

for d in move:
    nx, ny = x + dx[d-1], y + dy[d-1]
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    if d == 1:
        top, bottom, north, south, west, east = west, east, north, south, bottom, top
    elif d == 2:
        top, bottom, north, south, west, east = east, west, north, south, top, bottom
    elif d == 3:
        top, bottom, north, south, west, east = south, north, top, bottom, west, east
    else:   # d == 4
        top, bottom, north, south, west, east = north, south, bottom, top, west, east

    # 주사위 이동했을 때 지도 값이 0이면 주사위 값을 지도에 복사
    # 0이 아니면 지도 값을 주사위에 복사
    x, y = nx, ny
    if map_list[x][y] == 0:
        map_list[x][y] = bottom
    else:
        bottom = map_list[x][y]
        map_list[x][y] = 0

    print(top)

