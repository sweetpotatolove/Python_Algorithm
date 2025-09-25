import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    sell = 0
    total = 0
    for i in range(N-1, -1, -1):    # 뒤에서부터
        if price[i] > sell:     # 지금 가격이 최고가이면
            sell = price[i]     # 저장
        else:   # 최고가 아니면
            total += (sell - price[i])  # 저장된 최고가 - 지금가격
                                        # 현재 주식을 저장된 최고가의 날에 판거
    print(total)

    ''' 이중 for문으로 시간복잡도 O(N^2) -> 시간초과
    # 살지말지 결정
    buy = []
    for i in range(N):
        for j in range(i, N):
            if price[i] < price[j]:
                # 뒤에 오늘 가격보다 더 높은 가격인 날이 있다면 사자
                buy.append(i)
                break
    
    if not buy:
        print(0)
        continue

    # 팔지말지 결정
    total = 0
    for b in buy:   # 인덱스 들어가있음
        sell = 0
        for k in range(b+1, N):
            sell = max(sell, price[k])
        total += (sell - price[b])
    print(total)
    '''

