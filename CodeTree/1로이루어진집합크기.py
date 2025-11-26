from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 1. 컴포넌트 번호 부여 + 크기 계산
comp = [[-1] * m for _ in range(n)]
sizes = []
idx = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and comp[i][j] == -1:
            q = deque([(i, j)])
            comp[i][j] = idx
            s = 1

            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr, nc = r + dy[d], c + dx[d]
                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 1 and comp[nr][nc] == -1:
                            comp[nr][nc] = idx
                            q.append((nr, nc))
                            s += 1
            sizes.append(s)
            idx += 1

# 2. 0을 1로 바꿀 때 주변 컴포넌트 합산
max_cnt = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            adj = set()
            for d in range(4):
                nr, nc = i + dy[d], j + dx[d]
                if 0 <= nr < n and 0 <= nc < m and comp[nr][nc] != -1:
                    adj.add(comp[nr][nc])

            cnt = 1  # 자신을 1로 바꾸는 칸 포함
            for a in adj:
                cnt += sizes[a]

            max_cnt = max(max_cnt, cnt)

print(max_cnt)

