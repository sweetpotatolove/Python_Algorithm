T = int(input())


def dfs(num_sum, cnt, now):
    global result
    if cnt == N:
        result = min(result, num_sum + grid[now][0])
        # print(result)
        return

    for j in range(1, N):
        if used[j]:
            continue
        used[j] = True
        dfs(num_sum + grid[now][j], cnt + 1, j)
        used[j] = False

for test_case in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    result = float('inf')
    dfs(0, 1, 0)   # 사무실에서 무조건 시작
    print(f'#{test_case} {result}')