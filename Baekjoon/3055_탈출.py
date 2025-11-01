import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 비어있는 곳 '.', 물이 찬 곳 '*', 돌 'X'
# 비버 굴 'D', 고슴도치 위치 'S'

from collections import deque
고슴도치 = deque()
water = deque()
ay, ax = 0, 0
visited = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            고슴도치.append((i, j))
            visited[i][j] = True
        elif board[i][j] == '*':
            water.append((i, j))
        elif board[i][j] == 'D':
            ay, ax = i, j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
ok = False
while 고슴도치:
    for w in range(len(water)): # 물 퍼뜨리기
        wrow, wcol = water.popleft()
        for d in range(4):
            nwrow, nwcol = wrow + dy[d], wcol + dx[d]
            if 0 <= nwrow < R and 0 <= nwcol < C and board[nwrow][nwcol] == '.':
                board[nwrow][nwcol] = '*'
                water.append((nwrow, nwcol))
    
    for g in range(len(고슴도치)):
        grow, gcol = 고슴도치.popleft()
        # 성공 조건
        if grow == ay and gcol == ax:
            ok = True
            print(cnt)
            break
        for d in range(4):
            ngrow, ngcol = grow + dy[d], gcol + dx[d]
            if 0 <= ngrow < R and 0 <= ngcol < C and visited[ngrow][ngcol] == False:
                if board[ngrow][ngcol] == '.' or board[ngrow][ngcol] == 'D':
                    board[ngrow][ngcol] = 'S'
                    board[grow][gcol] = '.'
                    visited[ngrow][ngcol] = True
                    고슴도치.append((ngrow, ngcol))
    
    cnt += 1
    if ok:
        break

if ok == False:        
    print('KAKTUS')
