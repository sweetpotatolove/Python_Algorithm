# def solve(arr):
#     max_h = max(arr)
#     total_needed = 0
#     odd_needs = 0

#     # 1. 각 나무별로 필요한 높이와, 홀수 높이 필요 개수 파악
#     for h in arr:
#         diff = max_h - h
#         total_needed += diff

#         if diff % 2 != 0:
#             odd_needs += 1


#     # 이미 모든 키가 같다면 0일
#     if total_needed == 0:
#         return 0

#     # 2. 날짜를 1씩 증가시키며 최소 조건 확인
#     # 날짜(day)가 지날 때마다 공급 가능한 물의 양: 1, 2, 1, 2, ...
#     for day in range(1, 100000): # 충분히 큰 수까지 반복

#         # 현재 day까지의 홀수 날 개수 (1, 3, 5일...)
#         odd_days_available = (day + 1) // 2 

#         # 현재 day까지 공급할 수 있는 물의 최대 총합
#         # (홀수 날 개수 * 1) + (짝수 날 개수 * 2)
#         even_days_available = day // 2
#         max_capacity = odd_days_available * 1 + even_days_available * 2

#         # 조건 1: 총 물의 양이 필요한 양보다 크거나 같아야 함
#         # 조건 2: 홀수 크기를 처리할 수 있는 '홀수 날'이 충분해야 함
#         if max_capacity >= total_needed and odd_days_available >= odd_needs:
#             return day


# # # 전체 테스트 케이스 실행
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N = int(input())
# #     arr = list(map(int, input().split()))
# #     result = solve(arr)

# #     print(f"#{tc} {result}")


# def solve(arr):
#     max_h = max(arr)
#     total_diff = 0
#     odd_cnt = 0

#     for h in arr:
#         diff = max_h - h
#         total_diff += diff
#         if diff % 2 != 0:
#             odd_cnt += 1
    
#     if total_diff == 0:
#         return 0
    
#     for day in range(1, 100000):
#         # 현재 날짜까지 홀수 일 수 (1, 1, 2, 2, 3...)
#         odd_days = (day + 1) // 2

#         # 현재 날짜까지 짝수 일 수 (0, 1, 1, 2, 2...)
#         even_days = day // 2

#         # 현재 날짜까지 줄 수 있는 최대 물의 양
#         water = odd_days * 1 + even_days * 2

#         # 조건 1: 총량이 충분한가?
#         # 조건 2: 홀수 높이를 처리할 홀수 날이 충분한가?
#         if water >= total_diff and odd_days >= odd_cnt:
#             return day

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = solve(arr)  # 오타 수정 (sovle -> solve)
#     print(f'#{tc} {result}') # 출력 형식 수정 (# 추가)



# def solve(arr):
#     # 최대 나무 높이 계산
#     max_h = max(arr)

#     total_diff = 0
#     odd_cnt = 0
#     # 차이
#     for h in arr:
#         diff = max_h - h
#         total_diff += diff
#         if diff % 2 != 0:   # 홀수면 카운트
#             odd_cnt += 1
    
#     if total_diff == 0:
#         return 0
    
#     for day in range(1, 100000):
#         # 현재 날 까지 홀수 일 수
#         odd_days = (day + 1) // 2
#         # 현재 날 까지 짝수 일 수
#         even_days = day // 2

#         # 홀 + 짝 전체 물주기
#         water = odd_days * 1 + even_days * 2

#         # 조건 확인
#         if water >= total_diff and odd_days >= odd_cnt:
#             return day

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = solve(arr)
#     print(f'#{tc} {result}')



def solve(arr):
    # 최대 높이 계산
    max_h = max(arr)

    total_diff = 0
    odd_cnt = 0
    # 차이 계산
    for h in arr:
        diff = max_h - h
        total_diff += diff
        if diff % 2 != 0:
            odd_cnt += 1
    
    if total_diff == 0:
        return 0
    
    for day in range(1, 100000):
        # 현재 날짜까지 홀수 일 수
        odd_day = (day + 1) // 2

        # 현재 날짜까지 짝수 일 수
        even_day = day // 2

        # 전체 물 주기
        water = odd_day * 1 + even_day * 2

        # 조건
        if water >= total_diff and odd_day >= odd_cnt:
            return day
        

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(arr)
    print(f'#{tc} {result}')