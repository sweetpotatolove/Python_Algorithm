n = int(input())
block = [tuple(map(int, input().split())) for _ in range(n)]
grid = [[0] * 100 for _ in range(100)]

# 블럭 위치
for r, c in block:
    grid[r-1][c-1] = 1

# 블럭 하나 잡기
from collections import deque
oneblock = deque()
oneblock.append(block[0])
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[False] * 100 for _ in range(100)]
fr, fc = block[0]
visited[fr][fc] = True
result = 0
zeroblock = deque()
while oneblock:
    r, c = oneblock.popleft()
    cnt = 0
    for d in range(4):
        nr, nc = r + dy[d], c + dx[d]
        # 다음 위치가 블럭이면
        if 0 <= nr < 100 and 0 <= nc < 100 and grid[nr][nc] == 1:
            # 방문 안한 블럭이면 넣기
            if visited[nr][nc] == False:
                oneblock.append((nr, nc))
                visited[nr][nc] = True
            # 블럭 개수 세기
            cnt += 1
        # 블럭 근처 0 위치 수집
        if 0 <= nr < 100 and 0 <= nc < 100 and grid[nr][nc] == 0:
            zeroblock.append((nr, nc))
        
    
    # 테두리 개수 = 4 - cnt(블럭개수)
    result += (4 - cnt)

# 가운데 빈 블럭 찾기
visited_zero = [[False] * 100 for _ in range(100)]

while zeroblock:
    zr, zc = zeroblock.popleft()
    if visited_zero[zr][zc]:
        continue

    queue = deque()
    queue.append((zr, zc))
    visited_zero[zr][zc] = True
    zeros = [(zr, zc)]
    is_outside = False

    # BFS로 이 0덩어리 전체 탐색
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            # 격자 밖으로 나간다면 외부와 연결
            if not (0 <= ny < 100 and 0 <= nx < 100):
                is_outside = True
                continue
            # 주변에 아직 안 본 0칸이 있으면 계속 탐색
            if grid[ny][nx] == 0 and not visited_zero[ny][nx]:
                visited_zero[ny][nx] = True
                queue.append((ny, nx))
                zeros.append((ny, nx))

    # 내부 공백이라면 → 감산
    if not is_outside:
        for y, x in zeros:
            cnt = 0
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < 100 and 0 <= nx < 100 and grid[ny][nx] == 1:
                    cnt += 1
            result -= cnt

# 결과
print(result)

