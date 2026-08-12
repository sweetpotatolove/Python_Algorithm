# 프로그래머스 Lv2. 가장 큰 수
# 분류: 정렬
# 핵심: 두 수를 문자열로 이어붙였을 때(a+b vs b+a) 더 큰 조합이 앞에 오도록 정렬한 뒤 모두 이어붙여 가장 큰 수를 만든다.
# 시간 복잡도: O(n log n * L)
"""
    1. 입력 크기를 정의: numbers의 길이를 n, 각 수를 문자열로 바꿨을 때 최대 자릿수를 L이라 둔다.
    2. 코드에서 정렬·비교 연산의 비용을 입력 크기에 대한 함수로 센다.
    3. sorted(..., key=cmp_to_key(compare))는 O(n log n)번 비교를 수행하고, 매 비교(a+b vs b+a)는 문자열을 이어붙이고 비교하므로 O(L)이 걸린다.
        -> 전체 시간 = O(n log n) × O(L) = O(n log n * L)
"""


# 공간 복잡도: O(n * L)
"""
    1. 입력 자체를 저장하는 공간은 보통 제외하고(입력은 이미 주어진 것이므로), 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기에 비례해서 커지는 자료구조(리스트, 문자열 등)를 새로 만드는지 확인한다.
        -> 이 코드는 numbers를 문자열로 변환한 리스트(n개, 각 최대 L자)와 이를 이어붙인 answer 문자열(최대 n*L자)을 만드므로
        -> 추가 공간 = O(n * L)
"""


# 1. 문제 이해
# - 입력: 0 또는 양의 정수로 이루어진 배열 numbers
# - 출력: numbers의 원소들을 이어붙여 만들 수 있는 가장 큰 수(문자열)
# - 구해야 하는 것: 어떤 순서로 이어붙여야 결과가 가장 큰 수가 되는지


# 2. 아이디어
# - 두 수를 비교할 때 수 자체의 크기가 아니라, "이어붙였을 때의 결과"를 기준으로 비교해야 한다. 예: 3과 30은 330 vs 303이므로 3이 앞에 와야 한다(330 > 303).
# - 이 비교 규칙(a+b vs b+a)을 사용자 정의 비교 함수 compare로 만들고, cmp_to_key로 정렬 기준에 적용한다.
# - 정렬 후 문자열을 순서대로 이어붙이면 가장 큰 수가 만들어지는데, 모든 값이 0이면 "00...0" 형태가 되므로 이 경우만 "0"으로 따로 처리한다.


# 3. 풀이 계획
# 1) numbers의 각 원소를 문자열로 변환한다.
# 2) compare 함수(a+b와 b+a를 비교해 더 큰 조합이 앞에 오도록 -1/0/1을 반환)를 기준으로 cmp_to_key 정렬한다.
# 3) 정렬된 문자열들을 순서대로 이어붙여 answer를 만든다.
# 4) answer의 첫 글자가 '0'이면(모든 값이 0인 경우) '0'을 반환하고, 아니면 answer를 반환한다.


from functools import cmp_to_key

def compare(a, b):
    # a + b와 b + a를 비교
    # 누가 먼저 와야 하는지 반환
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))

    numbers = sorted(numbers, key=cmp_to_key(compare))

    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'

    return answer