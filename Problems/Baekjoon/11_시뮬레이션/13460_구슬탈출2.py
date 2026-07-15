from collections import deque
import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 빨간 구슬과 파란 구슬 위치 찾기
red_x = red_y = blue_x = blue_y = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        elif board[i][j] == 'B':
            blue_x, blue_y = i, j

def move(x, y, dx, dy):
    count = 0
    # 벽이 아니고 구멍이 아닐 때까지 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs():
    queue = deque()
    queue.append((red_x, red_y, blue_x, blue_y, 0))
    visited[red_x][red_y][blue_x][blue_y] = True

    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth >= 10:
            return -1

        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 빠지면 무효
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 두 구슬이 겹치면 이동 횟수 더 많은 쪽이 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs())
