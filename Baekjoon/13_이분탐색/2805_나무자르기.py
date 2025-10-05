import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0
while start <= end:
    mid = (start + end) // 2
    cut = 0
    for t in tree:
        if mid > t:
            continue
        else:
            cut += (t - mid)
            # print(f'{t} - {mid}, cut = {cut}')
    # print(f'total cut = {cut}')
    if cut < M: # 자른게 최소 길이보다 작으면 더 많이 잘라야함
                # 즉, 절단기 높이 낮추기
        end = mid - 1
    else: # 최소 길이보다 많이 잘랐으면 절단기 높이 늘려보기
        result = mid
        start = mid + 1

print(result)