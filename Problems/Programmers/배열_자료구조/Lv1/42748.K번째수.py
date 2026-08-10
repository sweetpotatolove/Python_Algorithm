# 프로그래머스 Lv1. K번째수
# 분류: 배열/정렬
# 핵심: 각 명령 [i, j, k]마다 array를 i번째부터 j번째까지 잘라 정렬한 뒤, k번째 원소를 뽑아 답 배열에 모은다.
# 시간 복잡도: O(m * n log n)
"""
    1. 입력 크기를 정의: array의 길이를 n, commands의 길이를 m이라 둔다.
    2. 코드에서 반복문·정렬의 실행 비용을 입력 크기에 대한 함수로 센다.
    3. commands를 순회하는 for문은 m번 실행되고, 매번 numbers.sort()가 최대 n개짜리 리스트를 정렬하므로 O(n log n)이 걸린다.
        -> 전체 시간 = m × O(n log n) = O(m * n log n)
"""


# 공간 복잡도: O(n)
"""
    1. 입력 자체를 저장하는 공간은 보통 제외하고(입력은 이미 주어진 것이므로), 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기에 비례해서 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> 이 코드는 매 명령마다 array를 슬라이싱한 numbers(최대 n개짜리 새 리스트)를 만들므로
        -> 추가 공간 = 구간 길이에 비례 = O(n)
"""


# 1. 문제 이해
# - 입력: 원본 배열 array, [i, j, k] 형태의 명령들이 담긴 2차원 배열 commands
# - 출력: 각 명령에 대해 i~j 구간을 자르고 정렬했을 때 k번째 수를 모은 배열
# - 구해야 하는 것: commands의 각 원소마다 "자르기 -> 정렬 -> k번째 값 뽑기"를 수행한 결과


# 2. 아이디어
# - commands를 순회하며 각 [i, j, k]에 대해 array를 슬라이싱(array[i-1:j])하고 정렬한 뒤, k-1번째(0-indexed) 값을 꺼낸다.
# - i, j, k는 1번째부터 세는 1-indexed 값이므로, 슬라이싱과 인덱싱에서 각각 1을 빼서 0-indexed로 맞춘다.
# - 각 명령의 결과를 answer 리스트에 순서대로 담는다.


# 3. 풀이 계획
# 1) 결과를 담을 answer 리스트를 준비한다.
# 2) commands의 각 [i, j, k]에 대해 array[i-1:j]로 구간을 잘라 numbers를 만든다.
# 3) numbers를 정렬한다.
# 4) 정렬된 numbers의 k-1번째 값을 answer에 추가한다.


def solution(array, commands):
    answer = []
    for command in commands:
        numbers = array[command[0]-1:command[1]]
        numbers.sort()
        answer.append(numbers[command[2]-1])

    return answer


"""
★ 개선 포인트 ★

array의 원소가 1~100 범위로 제한돼 있다는 게 핵심 힌트예요.
매 쿼리마다 구간을 잘라 정렬(O(len log len))하는 대신,
"값 1~100 각각이 인덱스 i까지 몇 번 등장했는지"를 미리 누적해두면
어떤 구간에서도 뺄셈 한 번으로 그 값의 등장 횟수를 O(1)에 구할 수 있어요.
그러면 k번째 값을 찾을 때 정렬 없이 값 1부터 100까지 훑으면서
누적 개수가 k를 넘는 순간의 값이 곧 답이 됩니다.

def solution(array, commands):
    n = len(array)
    V = 100  # 원소 값의 최댓값

    # prefix[i][v] = array의 앞 i개 중 값이 v인 원소의 개수
    prefix = [[0] * (V + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1][:]
        prefix[i][array[i-1]] += 1

    answer = []
    for i, j, k in commands:
        remaining = k
        for v in range(1, V + 1):
            count = prefix[j][v] - prefix[i-1][v]  # 구간 [i, j] 안에서 값 v의 개수
            if remaining <= count:
                answer.append(v)
                break
            remaining -= count

    return answer

# 시간 복잡도: O(n*V + m*V) - 전처리에 n×V, 쿼리마다 값 범위 V만큼 훑으므로 m×V. 구간 길이(len)에 더 이상 좌우되지 않는다.
# 공간 복잡도: O(n*V) - prefix 테이블 크기가 (n+1) × (V+1)
"""