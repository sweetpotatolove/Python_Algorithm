# 프로그래머스 Lv2. 프로세스
# 분류: 큐
# 핵심: 큐에서 꺼낸 프로세스보다 우선순위 높은 프로세스가 큐에 남아 있으면 다시 큐 뒤로 보내고,
#       없으면 그 프로세스를 실행(종료)한다. 이를 반복하며 실행된 순번을 센다.
# 시간 복잡도: O(n^3)
"""
    1. 바깥 while orders: 반복 횟수(=pop 횟수)
        - 최악의 입력(우선순위 오름차순, 예: [1,2,3,4])을 손으로 시뮬레이션하면:
        - 큐에 k개 남아있을 때, 그 중 1개가 실행되기까지 정확히 k번 pop이 필요 (나머지 k-1개는 재삽입, 1개만 실행)
        - 전체 pop 횟수 = n + (n-1) + ... + 1 = n(n+1)/2 → O(n²)
    2. 안쪽 for _, p in orders: 스캔 비용
        - 매 pop마다 남은 큐(최대 n개)를 훑음 → O(n)
    3. 합치면
        - O(n²)번의 pop, 각 pop마다 O(n) 스캔 → O(n²) × O(n) = O(n³)
"""

# 공간 복잡도: O(n)
"""
    orders = deque(enumerate(priorities)) 가 프로세스 개수만큼 (인덱스, 우선순위) 튜플을 담음 
    → 입력 크기에 비례
"""


# 1. 문제 이해
# - 입력: 프로세스 중요도 배열과 순서를 알고자하는 프로세스 위치
# - 출력: 입력 받은 프로세스의 실행 순서


# 2. 아이디어
# - (인덱스, 우선순위) 쌍을 큐에 넣고 앞에서부터 하나씩 꺼낸다.
# - 꺼낸 프로세스보다 우선순위가 높은 프로세스가 큐에 남아 있으면, 꺼낸 프로세스를 다시 큐 뒤로 넣는다.
# - 그런 프로세스가 없으면 꺼낸 프로세스를 실행하고 실행 순번을 1 증가시킨다.
# - 자료구조: 큐 (deque)


# 3. 풀이 계획
# 1) (인덱스, 우선순위)로 이루어진 deque를 만든다.
# 2) 큐가 빌 때까지 왼쪽에서 하나씩 꺼내며,
#    - 남은 큐 안에 우선순위가 더 높은 프로세스가 있으면 꺼낸 것을 다시 큐 뒤로 넣는다.
#    - 없으면 실행 순번(count)을 증가시키고, 실행된 인덱스가 찾는 location이면 count를 반환한다.

from collections import deque

def solution(priorities, location):
    
    orders = deque(enumerate(priorities))   # (인덱스, 우선순위) 큐 만들기
    # [2, 1, 3, 2] -> [(0, 2), (1, 1), (2, 3), (3, 2)]

    count = 0

    while orders:
        idx, priority = orders.popleft()

        ok = False
        for _, p in orders: 
            if priority < p:    # 지금 꺼낸 프로세스보다 우선순위 높은게 있으면
                ok = True
                break
        
        if ok:
            orders.append((idx, priority))
        else:
            count += 1
            if idx == location:
                return count


"""
★ 개선 포인트 ★

이 문제는 priorities[i]가 1~9 범위로 제한돼 있다는 게 핵심 힌트예요. 
"남은 큐에 나보다 우선순위 높은 게 있는가?"를 매번 큐 전체를 스캔해서 확인하지 않고, 
우선순위별 개수 배열(count array) 로 O(1)에 가깝게(최대 9번) 확인할 수 있습니다.

from collections import deque

def solution(priorities, location):
    orders = deque(enumerate(priorities))
    counts = [0] * 10                     # counts[p] = 큐에 남은 우선순위 p 개수
    for p in priorities:                  # counts:[0, 1, 2, 1, 0, 0, 0, 0, 0, 0]
        counts[p] += 1                              #  ↑  ↑  ↑
                                              # 우선순위1  2  3
                                                # 개수=1  개수=2 개수=1

    # "지금 꺼낸 프로세스보다 우선순위 높은 애가 큐에 남아있나?"를 확인할 때, 
    # 예를 들어 지금 꺼낸 게 우선순위 2라면:
    # counts[priority+1:]  # counts[3:] = [1, 0, 0, 0, 0, 0, 0]
    # any(counts[3:])       # → True (우선순위 3이 1개 있으니까)
    # 배열 전체를 순회하지 않고 counts[3]부터 끝까지만 슬라이싱해서 하나라도 0보다 크면 
    # "더 높은 우선순위가 남아있다"고 바로 알 수 있어요.

    count = 0
    while orders:
        idx, priority = orders.popleft()

        # 큐에 이 프로세스보다 우선순위 높은 게 남아있는지 O(9)만에 확인
        if any(counts[priority + 1:]):
            orders.append((idx, priority))
        else:
            counts[priority] -= 1
            count += 1
            if idx == location:
                return count
"""

p = list(map(int, input().strip("[]").split(",")))
l = int(input())
print(solution(p, l))
