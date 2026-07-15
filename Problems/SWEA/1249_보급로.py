T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    from collections import deque
    queue = deque([(0, 0, 0)])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    cost = [[float('inf')] * N for _ in range(N)]
    cost[0][0] = 0
    while queue:
        r, c, dist = queue.popleft()
        if cost[r][c] < dist:
            continue

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N:
                new_dist = dist + int(grid[nr][nc])
                if new_dist < cost[nr][nc]:
                    cost[nr][nc] = new_dist
                    queue.append((nr, nc, new_dist))

    print(f'#{test_case} {cost[N-1][N-1]}')