import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
ok = False
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, k, s, startx, starty):
    global ok
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == s:
            if visited[ny][nx] == True:
                if k >= 4 and nx == startx and ny == starty:
                    ok = True
                    return
            else:
                visited[ny][nx] = True
                dfs(nx, ny, k+1, s, startx, starty)

    return

for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]
        visited[i][j] = True
        dfs(j, i, 1, board[i][j], j, i)
        if ok:
            print('Yes')
            break
    if ok:
        break

if not ok:
    print('No')

    2500 * 4