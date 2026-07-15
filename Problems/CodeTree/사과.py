# def get_turn_cost(cur_dir, target_dir):
#     # 오른쪽 회전만 가능할 때 필요한 회전 수 (0~3)
#     return (target_dir - cur_dir + 4) % 4

# def solve(N, board):
#     # 1. 사과 위치 파악
#     apples = {}
#     for r in range(N):
#         for c in range(N):
#             if board[r][c] > 0:
#                 apples[board[r][c]] = (r, c)   # {1: (2,2) ..} 1번 사과 위치 (2,2)
    
#     # 2. 초기 상태 설정
#     curr_r, curr_c = 0, 0
#     curr_dir = 0  # 0:우, 1:하, 2:좌, 3:상 -> 오른쪽으로만 회전
#     total_turns = 0
    
#     # 3. 사과 순서대로 이동 시뮬레이션
#     # 사과 번호 1부터 M까지 (사과 개수는 len(apples))
#     for i in range(1, len(apples) + 1):
#         target_r, target_c = apples[i]  # i : 1 -> target_r = 2, target_c = 2
        
#         # 목표 방향 구하기
#         # 행 이동을 위해 필요한 방향
#         if target_r > curr_r: 
#             row_dir = 1   # 하
#         else: 
#             row_dir = 3   # 상
            
#         # 열 이동을 위해 필요한 방향
#         if target_c > curr_c: 
#             col_dir = 0   # 우
#         else: 
#             col_dir = 2   # 좌
        
#         # 경로 1: 세로(행) 이동 -> 가로(열) 이동
#         # 비용 = (현재->세로방향 회전) + (세로방향->가로방향 회전)
#         cost1 = get_turn_cost(curr_dir, row_dir) + get_turn_cost(row_dir, col_dir)
        
#         # 경로 2: 가로(열) 이동 -> 세로(행) 이동
#         # 비용 = (현재->가로방향 회전) + (가로방향->세로방향 회전)
#         cost2 = get_turn_cost(curr_dir, col_dir) + get_turn_cost(col_dir, row_dir)
        
#         # 두 경로 중 회전수가 적은 것 선택
#         if cost1 < cost2:
#             total_turns += cost1
#             curr_dir = col_dir # 최종적으로 가로 방향을 보게 됨
#         else:
#             total_turns += cost2
#             curr_dir = row_dir # 최종적으로 세로 방향을 보게 됨
            
#         # 위치 업데이트
#         curr_r, curr_c = target_r, target_c

#     return total_turns

# # 입력 처리
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     result = solve(N, board)
#     print(f"#{tc} {result}")


# def get_turn(from_dir, to_dir):
#     return (to_dir - from_dir + 4) % 4

# def solve(N, board):
#     # 사과 위치 찾기
#     apples = dict()
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] > 0:
#                 apples[board[i][j]] = (i, j)    # r, c
    
#     # 초기 상태 설정
#     curr_r, curr_c = 0, 0
#     curr_dir = 0    # 0:우, 1:하, 2:좌, 3:상
#     total_turn = 0

#     # 사과 시뮬
#     for a in range(1, len(apples) + 1):
#         target_r, target_c = apples[a]

#         # 행 비교
#         if target_r > curr_r:   # 크면 아래
#             row_dir = 1
#         else:
#             row_dir = 3
#         # 열 비교
#         if target_c > curr_c:   # 크면 오른쪽
#             col_dir = 0
#         else:
#             col_dir = 2
        
#         # 행 -> 열 cost
#         cost1 = get_turn(curr_dir, row_dir) + get_turn(row_dir, col_dir)
#         # 열 -> 행 cost
#         cost2 = get_turn(curr_dir, col_dir) + get_turn(col_dir, row_dir)

#         if cost1 <= cost2:
#             total_turn += cost1
#             curr_dir = col_dir
#         else:
#             total_turn += cost2
#             curr_dir = row_dir
        
#         curr_r, curr_c = target_r, target_c
    
#     return total_turn

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     result = solve(N, board)
#     print(f"#{tc} {result}")



def get_turn(now, next):
    return (next - now + 4) % 4

def solve(n, arr):
    # 사과 위치 찾기
    apples = dict()
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                apples[board[i][j]] = (i, j)    # r, c
    
    # 초기화
    curr_r, curr_c = 0, 0
    curr_dir = 0    # 0: 우, 1: 하, 2: 좌, 3: 상
    total_turn = 0

    for a in range(1, len(apples) + 1):
        target_r, target_c = apples[a]

        # 행 비교
        if target_r > curr_r:   # 크면 아래
            row_dir = 1
        else:
            row_dir = 3
        
        # 열 비교
        if target_c > curr_c:   # 크면 오른쪽
            col_dir = 0
        else:
            col_dir = 2
        
        # 행 방향 -> 열 방향 / 열 방향 -> 행 방향 cost 비교
        cost1 = get_turn(curr_dir, row_dir) + get_turn(row_dir, col_dir)
        cost2 = get_turn(curr_dir, col_dir) + get_turn(col_dir, row_dir)

        if cost1 <= cost2:
            curr_dir = col_dir
            total_turn += cost1
        else:
            curr_dir = row_dir
            total_turn += cost2
        
        curr_r, curr_c = target_r, target_c
    
    return total_turn


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = solve(n, board)
    print(f'#{tc} {result}')