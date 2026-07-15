T = int(input())
def dfs(idx, num_sum):
    # idx: 현재 위치
    # num_sum: 합산
    global cnt
    if num_sum == K:
        cnt += 1
        return
    if num_sum > K:
        return

    for j in range(idx, N):
        # 지금 위치 다음거부터 더해봄
        # 만약 더했을때 K 넘었으면 스킵

        # 더하는 경우
        dfs(j + 1, num_sum + numbers[j])


    return

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    dfs(0, 0)
    print(cnt)