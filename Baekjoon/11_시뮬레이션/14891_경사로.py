import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def can_go(road, L):
    used = [False] * len(road)
    for i in range(len(road) - 1):
        if road[i] == road[i+1]:
            continue
        elif road[i] - road[i+1] == 1:  # 내려가는 경사로
            for j in range(i+1, i+1+L):
                if j >= len(road) or road[j] != road[i+1] or used[j]:
                    return False
                used[j] = True
        elif road[i] - road[i+1] == -1:  # 올라가는 경사로
            for j in range(i, i-L, -1):
                if j < 0 or road[j] != road[i] or used[j]:
                    return False
                used[j] = True
        else:
            return False
    return True

count = 0

# 행 검사
for row in board:
    if can_go(row, L):
        count += 1

# 열 검사
for c in range(N):
    col = [board[r][c] for r in range(N)]
    if can_go(col, L):
        count += 1

print(count)
