import sys
input = sys.stdin.readline

def dfs(idx, w):
    global maxP
    temp = 1
    for k in range(len(w)):
        temp *= (P[k][w[k]] / 100)

    if maxP > temp:
        return

    if idx == N:
        if maxP < temp:
            maxP = temp
        return

    for i in range(N):
        # i번째 선택 O
        if visited[i] == False:
            visited[i] = True
            dfs(idx + 1, w + [i])
            visited[i] = False
    return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    work = []
    maxP = 0
    dfs(0, [])
    print(f'#{test_case} {maxP * 100:.6f}')
