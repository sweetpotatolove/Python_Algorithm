import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def make_curve(d, g):
    dirs = [d]
    for _ in range(g):
        for prev in reversed(dirs):
            dirs.append((prev + 1) % 4)
    return dirs

board = [[0]*101 for _ in range(101)]

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    dirs = make_curve(d, g)
    for dir in dirs:
        x += dx[dir]
        y += dy[dir]
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = 1

# 네 꼭짓점 모두 포함된 1x1 정사각형 카운트
ans = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y][x+1] and board[y+1][x] and board[y+1][x+1]:
            ans += 1

print(ans)
