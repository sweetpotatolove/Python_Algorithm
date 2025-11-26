N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0]
dy = [0, 1]


# Please write your code here.
def dfs(r, c, cnt, now):
    global max_coin

    # 민약 k개에 놨다면 그만
    if cnt == K:
        max_coin = max(now, max_coin)
        return

    # 격자 놨던 자리면 넘어가기
    if visited[r][c] == True:
        return

    # 지금 칸에 격자 놓기
    for i in range(2):
        nr, nc = r + dy[i], c + dx[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
            visited[r][c] = True
            visited[nr][nc] = True  # 격자 놓음

            # 다음 위치
            nextc, nextr = (c + 1) % N, r
            if (c + 1) == N:
                nextr += 1
                if nextr == N:
                    return

            dfs(nextr, nextc, cnt + 1, now + grid[r][c] + grid[nr][nc])
            visited[nr][nc] = False
            visited[r][c] = False

    # 선택x
    nextc, nextr = (c + 1) % N, r
    if (c + 1) == N:
        nextr += 1
        if nextr == N:
            return
        else:
            dfs(nextr, nextc, cnt, now)

    return


visited = [[False] * N for _ in range(N)]
max_coin = 0
dfs(0, 0, 0, 0)
print(max_coin)