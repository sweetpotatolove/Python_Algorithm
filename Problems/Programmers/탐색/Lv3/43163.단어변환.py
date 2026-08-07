# 프로그래머스 Lv3. 단어 변환
# 분류: 완전탐색(DFS + 백트래킹)
# 핵심: 현재 단어와 알파벳이 하나만 다른, 아직 방문하지 않은 단어로 매번 이동해보며 target까지의 모든 경로를 DFS로 탐색하고, 그중 변환 횟수가 최소인 경로를 찾는다.
# 시간 복잡도: O(n! * n * L) (최악의 경우, n=words 개수, L=단어 길이)
"""
    1. 입력 크기를 정의: words의 길이를 n(단어 개수), 각 단어의 길이를 L이라 둔다.
    2. dfs 한 번을 호출할 때마다 words를 순회(n번)하며 각 단어와의 diff를 계산(O(L))하므로, 호출 한 번의 비용은 O(n*L)이다.
    3. 가지치기 없이 방문하지 않은 단어로 재귀 호출을 하고 백트래킹으로 되돌아오므로, 방문 순서(순열)를 전부 시도할 수 있다.
        -> 최악의 경우 dfs 호출 횟수는 n!에 가까워지고,
        -> 호출마다 O(n*L)의 비용이 들므로
        -> 전체 시간 = O(n! * n * L) (n, L 모두 문제 제한상 최대 50 수준)
"""


# 공간 복잡도: O(n^2)
"""
    1. 입력 자체를 저장하는 공간은 보통 제외하고(입력은 이미 주어진 것이므로), 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기 n에 비례해서 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> 이 코드는 visited 배열(길이 n)을 사용하고, 재귀 호출 깊이가 최대 n까지 쌓이며 각 호출 프레임마다 results 리스트(최대 크기 n)를 새로 만드므로
        -> 추가 공간 = 재귀 깊이 × 프레임당 공간 = O(n) × O(n) = O(n^2)
"""


# 1. 문제 이해
# - 입력: 시작 단어 begin, 목표 단어 target, 단어 집합 words
# - 출력: begin에서 target까지 변환하는 데 필요한 최소 단계 수, 변환할 수 없으면 0
# - 구해야 하는 것: 한 번에 알파벳 하나만 바꾸고 words에 있는 단어로만 이동할 수 있다는 규칙에서, begin -> target 최소 변환 횟수


# 2. 아이디어
# - 현재 단어에서 알파벳이 정확히 하나만 다른, 아직 방문하지 않은 단어로 갈 수 있다고 보고 DFS로 모든 경로를 탐색한다(백트래킹으로 방문 표시를 되돌리며 다른 경로도 시도).
# - target에 도달하면 지금까지의 변환 횟수(cnt)를 그대로 반환하고, 여러 경로로 도달했다면 그중 최솟값을 선택한다.
# - 더 이상 갈 수 있는 단어가 없으면 그 경로는 실패로 보고 0을 반환하며, 결과 취합 시 0은 제외된다.


# 3. 풀이 계획
# 1) visited 배열(길이 len(words), 모두 False)을 만들고 dfs(begin, target, 0, words, visited)를 호출한다.
# 2) dfs에서 현재 단어가 target과 같으면 지금까지의 변환 횟수 cnt를 그대로 반환한다.
# 3) 아직 방문하지 않은 각 단어에 대해 현재 단어와 알파벳이 몇 개 다른지(diff) 센다.
# 4) diff가 1이면 그 단어를 방문 처리하고 cnt+1로 재귀 호출한 뒤, 결과가 0이 아니면 results에 담고 다시 방문 해제(백트래킹)한다.
# 5) 모든 후보를 다 확인하면 results 중 최솟값을 반환하고, results가 비어 있으면(더 갈 곳이 없으면) 0을 반환한다.


def dfs(now, target, cnt, words, visited):
    if now == target:
        return cnt

    results = [] # 현재 dfs 호출 안에서만 사용하는 리스트
    for idx in range(len(words)):
        if not visited[idx]:
            diff = 0
            for i in range(len(now)):
                if now[i] != words[idx][i]:
                    diff += 1

            # 한 개의 알파벳만 다를 때 거기로 감
            if diff == 1:
                visited[idx] = True
                result = dfs(words[idx], target, cnt + 1, words, visited)

                if result != 0:
                    results.append(result)

                visited[idx] = False

    if results:
        return min(results)

    # 다 봤는데 갈 곳 없으면
    return 0

def solution(begin, target, words):
    visited = [False] * len(words)
    answer = dfs(begin, target, 0, words, visited)

    return answer


"""
★ 개선 포인트 ★

"최소 변환 횟수"를 구하는 문제는 그래프의 최단 거리 문제와 같아요.
지금 풀이는 DFS + 백트래킹으로 target까지 가능한 경로를 전부 탐색한 뒤 그중 최솟값을 고르는 방식이라,
가지치기가 없어서 최악의 경우 방문 순서(순열)를 거의 다 시도하는 O(n!) 수준까지 커질 수 있어요.

BFS는 "가까운 단어부터" 순서대로 방문하기 때문에, target을 처음 방문하는 순간이 곧 최단 거리예요.
그래서 굳이 모든 경로를 끝까지 탐색하고 최솟값을 비교할 필요 없이, target에 도달하자마자 바로 반환하면 됩니다.

from collections import deque

def solution(begin, target, words):
    if target not in words:      # target이 words에 없으면 애초에 도달 불가능
        return 0

    queue = deque([(begin, 0)])
    visited = {begin}

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt

        for w in words:
            if w not in visited and sum(a != b for a, b in zip(word, w)) == 1:
                visited.add(w)
                queue.append((w, cnt + 1))

    return 0

# 시간 복잡도: O(n^2 * L) - 단어 하나당 큐에서 한 번만 꺼내지고(n번), 꺼낼 때마다 나머지 단어 n개와 diff를 O(L)에 비교하므로 n × n × L = O(n^2 * L)
# 공간 복잡도: O(n) - visited 집합과 queue에 담기는 원소가 최대 n개
"""