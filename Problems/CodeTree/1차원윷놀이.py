n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
location = [1] * (k+1)
def dfs(idx):
    # idx: 이동 가능한 거리들 인덱스
    global result

    # 더이상 이동할 수 없으면 끝
    if idx == len(nums):
        cnt = 0
        # print(location)
        for check in location:
            if check >= m:
                cnt += 1
        result = max(cnt, result)
        return
    
    # 돌아가면서 해당 거리 말 내보내기
    for h in range(1, k+1):
        if location[h] >= m:
            continue
        # print(f'{h}번째 말 선택: {nums[idx]} 전진, 위치: {location[h] + nums[idx]}')
        location[h] += nums[idx]
        dfs(idx + 1)
        location[h] -= nums[idx]
    
    # 만약 모든 말이 m을 넘어섰다면? 여기로 올듯
    cnt = 0
    for check in location:
        if check >= m:
            cnt += 1
    result = max(cnt, result)
    
result = 0
dfs(0)
print(result)