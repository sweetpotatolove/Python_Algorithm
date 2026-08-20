


# 프로그래머스 Lv2. 다리를 지나는 트럭
# 분류: 큐 시뮬레이션(시간 점프 최적화)
# 핵심: 다리 위 트럭들을 (무게, 빠져나가는 시각) 쌍으로 큐에 저장해두고, 매 시각마다 빠져나갈 트럭을 먼저 내린 뒤 다음 트럭을 올릴 수 있는지 확인한다. 올릴 수 없을 때는 1초씩 흘리는 대신 다리 맨 앞 트럭이 빠져나가는 시각으로 time을 바로 점프시켜 불필요한 반복을 줄인다.
# 시간 복잡도: O(k) (k = 트럭 개수)
"""
    1. 입력 크기를 정의: 트럭의 개수를 k(len(truck_weights))라 하자.
    2. 코드에서 반복문의 실행 횟수를 입력 크기에 대한 함수로 센다.
        -> while wating: 대기 중인 트럭이 모두 다리에 올라갈 때까지 반복하는데,
        -> 트럭을 올릴 수 없을 때는 1초씩 흘리지 않고 다리 맨 앞 트럭이 빠져나가는 시각으로 time을 바로 점프시키므로
        -> 반복 횟수는 트럭이 다리에 오르내리는 사건 수, 즉 k에 비례한다.
        -> 반복문 내부의 popleft, append, 비교 연산은 모두 O(1)이다.
    3. 따라서 전체 시간 = k × O(1) = O(k)
"""


# 공간 복잡도: O(k)
"""
    1. 입력 자체를 저장하는 공간은 제외하고, 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기 k에 비례해서 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> 이 코드는 bridge와 wating 두 개의 큐를 사용하는데, 이 둘에 들어있는 트럭의 총 개수는 항상 입력 트럭 개수 k 이하이므로
        -> 추가 공간 = O(k)
"""


# 1. 문제 이해
# - 입력: 다리의 길이 bridge_length, 다리가 견딜 수 있는 최대 무게 weight, 순서대로 다리를 건너야 하는 트럭들의 무게 목록 truck_weights
# - 출력: 모든 트럭이 다리를 건너는 데 걸리는 총 시간
# - 구해야 하는 것: 트럭은 1초에 다리 한 칸씩 이동하며, 다리 위 트럭 무게의 합이 weight를 넘지 않는 선에서 트럭을 순서대로 올려 마지막 트럭이 다리를 완전히 빠져나가는 시각


# 2. 아이디어
# - 다리에 올라간 트럭이 몇 초 뒤에 빠져나가는지는 (올라간 시각 + bridge_length)로 미리 계산할 수 있으므로, 다리 위 트럭을 (무게, 빠져나가는 시각) 쌍으로 큐에 저장한다.
# - 매 시각(time)마다 먼저 다리 맨 앞 트럭이 빠져나갈 시각이 됐는지 확인해 빠져나가면 bridge_weight에서 그 무게를 빼고, 그 다음 대기 중인 트럭을 올릴 수 있는지(bridge_weight + 다음 트럭 무게 <= weight) 확인한다.
# - 트럭을 올릴 수 없는 경우 1초씩 흘리며 확인하면 시간이 오래 걸리므로, 다리 맨 앞 트럭이 빠져나가는 시각 직전으로 time을 바로 점프시켜 반복 횟수를 줄인다.
# - 대기 트럭이 모두 다리에 올라가면 반복을 종료하고, 다리에 마지막으로 올라간 트럭이 빠져나가는 시각이 곧 전체 트럭이 다리를 건너는 데 걸린 총 시간이다.


# 3. 풀이 계획
# 1) 다리 위 트럭을 담을 bridge 큐, 대기 중인 트럭을 담을 wating 큐(truck_weights), 다리 위 트럭 무게 합 bridge_weight, 현재 시각 time을 초기화한다.
# 2) wating이 빌 때까지 time을 1씩 늘리며 반복한다.
# 3) 다리 맨 앞 트럭의 빠져나가는 시각이 현재 time 이하이면 그 트럭을 내리고 bridge_weight에서 무게를 뺀다.
# 4) bridge_weight + 대기 중인 다음 트럭 무게가 weight 이하이면 그 트럭을 다리에 올리고(bridge_weight에 무게를 더하고, 빠져나가는 시각 = time + bridge_length로 큐에 저장), 아니라면 time을 다리 맨 앞 트럭이 빠져나가는 시각 - 1로 점프시킨다.
# 5) wating이 비면 반복을 종료하고, 다리에 마지막으로 올라간 트럭이 빠져나가는 시각(bridge[-1][1])을 반환한다.


from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    wating = deque(truck_weights)
    bridge_weight = 0
    time = 0

    while wating:
        time += 1
        # 다리에 트럭 뺄 수 있는지 확인
        if bridge and bridge[0][1] <= time:
            truck, exit_time = bridge.popleft()
            bridge_weight -= truck

        # 다리에 트럭 올라갈 수 있으면
        if bridge_weight + wating[0] <= weight:
            truck = wating.popleft()
            bridge_weight += truck
            bridge.append((truck, time + bridge_length))
        # 올라갈 수 없으면 -> 시간 스킵
        else:
            time = bridge[0][1] - 1

    # 모든 트럭이 다리를 건넜거나 다리위에 있으면
    return bridge[-1][1]


# 아래는 시간 초과가 발생한 첫 시도 코드
# 시간 복잡도: O(n²L + nL²)  (n = 트럭 개수, L = bridge_length)
"""
    1. 입력 크기를 정의: 트럭 개수를 n(len(truck_weights)), 다리 길이를 L(bridge_length)라 하자.
    2. while 반복문은 1초씩 시간을 흘리며 모든 트럭이 다리를 건널 때까지 반복하므로, 반복 횟수는 총 이동 시간(answer)과 같다.
        -> 최악의 경우(무게 제한 때문에 트럭이 한 번에 한 대씩만 다리에 오를 수 있을 때) 트럭마다 다리를 완전히 빠져나가는 데 L초씩 필요하므로 총 이동 시간은 O(n × L)이다.
    3. 반복문 내부에서 sum(finish)(while 조건)와 sum(bridge)를 매번 새로 계산하는데, finish의 길이는 최대 n, bridge의 길이는 항상 L이므로 한 번의 반복 비용은 O(n + L)이다.
    4. 따라서 전체 시간 = 반복 횟수 × 반복문 내부 비용 = O(n × L) × O(n + L) = O(n²L + nL²)
    -> n, L이 각각 최대 10,000에 가까운 값까지 커질 수 있어 시간 초과가 발생한다.
    -> 개선된 코드는 sum() 재계산 대신 bridge_weight를 누적 관리하고, 트럭을 못 올릴 때 1초씩 흘리는 대신 time을 바로 점프시켜 반복 횟수와 반복당 비용을 모두 줄였다(O(n)).
"""
""" 시간초과
def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    finish = []
    f_sum = sum(truck_weights)  # 다리를 지나야하는 트럭 개수
    answer = 0
    while sum(finish) < f_sum:
        answer += 1
        finish.append(bridge.popleft()) # 일단 다리에 있는거 건너고

        # 대기 중인거 다리에 놓을 수 있는지 확인
        if truck and ((sum(bridge) + truck[0]) <= weight): 
            bridge.append(truck.popleft())
        else:
            bridge.append(0)

    return answer
    """