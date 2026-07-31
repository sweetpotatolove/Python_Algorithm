# 프로그래머스 Lv3. 네트워크
# 분류: 완전탐색(BFS)
# 핵심: 인접행렬 computers를 그래프로 보고, 방문하지 않은 컴퓨터를 만날 때마다 새 네트워크로 세면서 BFS로 연결된 컴퓨터를 모두 방문 처리한다.
# 시간 복잡도: O(n^2)
"""
    1. 입력 크기를 정의: 컴퓨터 개수를 n이라 하면, computers는 n×n 크기의 인접행렬이다.
    2. 코드에서 반복문·조건문의 실행 횟수를 입력 크기에 대한 함수로 센다.
    3. 상수 시간 연산(비교, 대입, 인덱스 접근)은 O(1)로 취급하고, 이런 연산이 반복문 안에서 몇 번 실행되는지 곱한다.
        -> for i in range(n): n번 실행되지만 이미 방문한 컴퓨터는 continue로 넘어간다.
        -> BFS(while queue)는 각 컴퓨터를 정확히 한 번씩 방문하므로 전체 방문 횟수는 n번이고,
        -> 방문할 때마다 for next in range(n): n번씩 인접행렬을 확인하므로
        -> 전체 시간 = n × n × O(1) = O(n^2)
"""


# 공간 복잡도: O(n)
"""
    1. 입력 자체를 저장하는 공간은 보통 제외하고(입력은 이미 주어진 것이므로), 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기 n에 비례해서 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> 이 코드는 visited 배열(길이 n)과 BFS용 queue(최대 n개 원소)를 사용하므로
        -> 추가 공간 = 컴퓨터 수에 비례 = O(n)
"""


# 1. 문제 이해
# - 입력: 컴퓨터 개수 n, n×n 크기의 연결 정보 인접행렬 computers
# - 출력: 네트워크(연결 요소)의 개수
# - 구해야 하는 것: 직접 또는 간접으로 연결된 컴퓨터들의 묶음이 총 몇 개인지


# 2. 아이디어
# - computers를 그래프의 인접행렬로 보고, 아직 방문하지 않은 컴퓨터를 시작점으로 BFS를 수행해 연결된 컴퓨터를 모두 방문 처리한다.
# - 새로운 시작점을 잡을 때마다 아직 어떤 네트워크에도 속하지 않았던 컴퓨터를 발견한 것이므로, 그때마다 answer를 1 증가시킨다.
# - 모든 컴퓨터를 순회할 때까지 반복하면, answer는 결국 네트워크(연결 요소)의 개수가 된다.


# 3. 풀이 계획
# 1) visited 배열(길이 n, 모두 False)과 answer(0)를 준비한다.
# 2) 0번부터 n-1번 컴퓨터까지 순회하며, 이미 방문한 컴퓨터는 건너뛴다.
# 3) 방문하지 않은 컴퓨터를 만나면 새로운 네트워크로 세고(answer += 1), 그 컴퓨터를 시작점으로 BFS를 수행한다.
# 4) BFS에서 큐에서 컴퓨터를 꺼내 인접행렬을 확인하며, 연결되어 있고 아직 방문하지 않은 컴퓨터를 방문 처리 후 큐에 넣는다.


from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:   # 이미 방문했으면 넘어감
            continue

        # 새로운 네트워크 발견
        answer += 1

        queue = deque([i])
        visited[i] = True

        while queue:
            cur = queue.popleft()

            # 연결된 컴퓨터 탐색
            for next in range(n):
                if computers[cur][next] == 1:
                    if not visited[next]:
                        visited[next] = True
                        queue.append(next)

    return answer