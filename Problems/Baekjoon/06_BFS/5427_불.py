import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for test_case in range(T):
    w, h = map(int, input().split())
    building_map = [list(input().strip()) for _ in range(h)]
    
    # 상근이 위치 찾기
    sang_location = deque()
    fire = deque()
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if building_map[i][j] == '@':
                sang_location.append((i, j))
                visited[i][j] = True
            elif building_map[i][j] == '*':
                fire.append((i, j))

    ok = False
    cnt = 0
    while sang_location:
        for j in range(len(fire)):  # 지금 불 있는것들 다 번지게 해야함
            frow, fcol = fire.popleft()
            for k in range(4):
                fny, fnx = frow + dy[k], fcol + dx[k]
                if 0 <= fny < h and 0 <= fnx < w and building_map[fny][fnx] == '.':
                    building_map[fny][fnx] = '*'
                    fire.append((fny, fnx))

        for i in range(len(sang_location)):
            row, col = sang_location.popleft()

            # 성공 조건
            # 상근이가 가장자리에 도착하면 됨
            if row == 0 or row == h-1 or col == 0 or col == w-1:
                print(cnt + 1)
                ok = True
                break

            for k in range(4):
                ny, nx = row + dy[k], col + dx[k]
                if 0 <= ny < h and 0 <= nx < w:
                    if building_map[ny][nx] == '.' and visited[ny][nx] == False:     # 상근이가 갈 수 있는 길이면
                        visited[ny][nx] = True     # 가자
                        sang_location.append((ny, nx))
        cnt += 1
        if ok:
            break
    
    if ok == False:
        print("IMPOSSIBLE")


