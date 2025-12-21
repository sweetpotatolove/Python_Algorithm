# def max_two_k_segments_sum(n, k, arr):
#     # K 길이의 부분합 계산
#     window_sum = [0] * (n - k + 1)
#     curr_sum = sum(arr[:k])
#     window_sum[0] = curr_sum
#     for i in range(1, n - k + 1):
#         curr_sum = curr_sum - arr[i - 1] + arr[i + k - 1]
#         window_sum[i] = curr_sum

#     # 최대 합 계산 (두 구간이 겹치지 않게)
#     max_sum = float('-inf')
#     # 왼쪽 구간 [i], 오른쪽 구간 [j] (j >= i + k)
#     max_left = window_sum[0]
#     for j in range(k, len(window_sum)):
#         max_left = max(max_left, window_sum[j - k])
#         max_sum = max(max_sum, max_left + window_sum[j])

#     return max_sum

# # 입력 처리
# T = int(input())
# for tc in range(1, T + 1):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = max_two_k_segments_sum(n, k, arr)
#     print(f"#%d %d" % (tc, result))


# def max_k_sum(n, k, arr):
#     # 윈도우 배열 만들기
#     window_sum = [0] * (n-k+1)
#     curr_sum = sum(arr[:k])
#     window_sum[0] = curr_sum

#     # 윈도우 배열 채우기
#     for i in range(1, n-k+1):
#         curr_sum = curr_sum - arr[i-1] + arr[i+k-1]
#         window_sum[i] = curr_sum
    
#     # 왼 i 오 j
#     # j >= i + k
#     max_sum = float('-inf')
#     max_left = window_sum[0]
#     for j in range(k, len(window_sum)):
#         max_left = max(max_left, window_sum[j-k])
#         max_sum = max(max_sum, max_left + window_sum[j])
    
#     return max_sum


# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = max_k_sum(n, k, arr)
#     print(f'#{tc} {result}')



def max_k_sum(n, k, arr):
    # 윈도우 배열 만들기
    window_sum = [0] * (n - k + 1)
    curr_sum = sum(arr[:k])
    window_sum[0] = curr_sum

    # 윈도우 배열 채우기
    for i in range(1, n - k + 1):
        curr_sum = curr_sum - arr[i - 1] + arr[i + k - 1]
        window_sum[i] = curr_sum
    
    # 오른쪽 j >= 왼쪽 i + k
    max_sum = float('-inf')
    max_left = window_sum[0]
    for j in range(k, len(window_sum)):
        max_left = max(max_left, window_sum[j - k])
        max_sum = max(max_sum, max_left + window_sum[j])
    
    return max_sum

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = max_k_sum(n, k, arr)
    print(f'#{tc} {result}')