# 프로그래머스 Lv2. 타겟 넘버
# 분류: 탐색(DFS)
# 핵심: 각 숫자마자 + 또는 - 두 가지를 모두 탐색하여 타겟 넘버 만드는 경우의 수 구하기
# 시간 복잡도: O(2^n)
# 공간 복잡도: O(n)


# 1. 문제 이해
# - 입력: 숫자 배열(numbers), 목표 숫자(target)
# - 출력: 숫자에 '+', '-'를 붙여 타겟 넘버 만드는 경우의 수
# - 구해야 하는 것: 모든 숫자를 순서대로 사용하면서 더하거나 빼는 모든 경우를 탐색하여 target을 만드는 경우의 수


# 2. 아이디어
# - 각 숫자는 '+' 또는 '-' 선택 가능
# - DFS 활용하여 모든 경우 탐색
# - 모든 숫자를 사용했을 때 타겟 넘버와 동일하면 1 반환 (아니면 0)


# 3. 풀이 계획
# 1) dfs 정의
# 2) 모든 숫자를 사용했을 때 total이 target인지 확인 -> 맞으면 카운트 1
# 3) 현재 숫자 더하는 경우랑 빼는 경우 재귀 호출해서 더함으로써, 현재 상태에서 만들 수 있는 경우의 수 반환


def solution(numbers, target):
    answer = 0
    
    def dfs(idx, total):
        
        # 모든 숫자 사용
        if idx == len(numbers):
            # 타겟 넘버랑 같은지 확인
            if total == target:
                return 1
            else:
                return 0

        # 현재 숫자 더하는 경우 + 현재 숫자 빼는 경우
        return (dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx]))
                
    answer = dfs(0, 0)

    return answer