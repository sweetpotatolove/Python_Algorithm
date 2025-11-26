import sys
input = sys.stdin.readline
T = int(input())

def dfs(idx, s):
    global result
    # print(idx, s)
    if idx == N:
        if s >= B:
            if (s - B) < result:
                result = s - B
        return

    if s >= B:  # 합이 탑보다 크면 계산
        if (s - B) < result:
            result = s - B
        return

    # 현재 직원 선택O
    dfs(idx + 1, s + H[idx])
    # 현재 직원 선택X
    dfs(idx + 1, s)
    return

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    result = float('inf')
    dfs(0, 0)
    print(f'#{test_case} {result}')
