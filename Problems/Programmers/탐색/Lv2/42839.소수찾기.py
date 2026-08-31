# 프로그래머스 Lv2. 소수 찾기
# 분류: 완전탐색(순열, 소수 판별)
# 핵심: 종이 조각으로 만들 수 있는 길이 1~n의 모든 순열을 정수로 바꿔 후보를 모으고, 중복을 제거한 뒤 각 후보가 2부터 자기 자신 전까지 나누어떨어지는 수가 없는지 확인해 소수 개수를 센다.
# 시간 복잡도: O(n! × 10^n)
"""
    1. 입력 크기를 정의: numbers의 자릿수(길이)를 n이라 하자 (n <= 7).
    2. 코드에서 반복문의 실행 횟수를 입력 크기에 대한 함수로 센다.
        -> for i in range(1, n+1)과 permutations(num_list, i): 길이 i(1~n)별로 만들 수 있는 순열의 총 개수는 sum_{i=1}^{n} nPi ≈ O(n!)이고,
        -> 순열 하나마다 "".join(j)과 int() 변환에 O(n)이 걸리므로 조합 생성 단계는 O(n × n!)이다.
        -> for num in set(comb_list): 최대 O(n!)개의 서로 다른 후보를 순회하며, 각 후보마다 for x in range(2, num)으로 소수 판별을 하는데
        -> num은 최대 10^n - 1까지 커질 수 있으므로 이 단계는 최악 O(n! × 10^n)이다.
    3. 따라서 전체 시간 = O(n × n!) + O(n! × 10^n) = O(n! × 10^n)
"""


# 공간 복잡도: O(n × n!)
"""
    1. 입력 자체를 저장하는 공간은 제외하고, 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기에 비례해 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> comb_list는 길이 1~n의 모든 순열을 정수로 저장하므로 최대 O(n!)개의 원소를 담고, 각 원소는 최대 n자리 숫자이므로
        -> 추가 공간 = O(n × n!)
"""


# 1. 문제 이해
# - 입력: 숫자가 적힌 종이 조각들을 나타내는 문자열 numbers (0~9로 이루어진 숫자 문자, 최대 7자리)
# - 출력: numbers에 적힌 종이 조각을 일부 또는 전부 사용해 만들 수 있는 서로 다른 소수의 개수
# - 구해야 하는 것: 종이 조각의 순서를 바꿔가며 나열해 만들 수 있는 모든 수 중, 소수인 값이 몇 개인지


# 2. 아이디어
# - "일부 또는 전부를 사용"하므로 길이 1부터 numbers 전체 길이까지 모든 순열을 구해야 한다.
# - itertools.permutations로 각 길이별 순열을 구해 문자열로 이어붙인 뒤 정수로 바꾸면 만들 수 있는 모든 후보 수를 얻을 수 있다.
# - 같은 숫자가 여러 조합에서 중복으로 만들어질 수 있으므로 set으로 중복을 제거한 뒤, 각 후보가 2 이상이면서 2부터 자기 자신 전까지 나누어떨어지는 값이 없는지 확인해 소수 여부를 판별한다.


from itertools import permutations
def solution(numbers):
    num_list = []
    for number in numbers:
        num_list.append(number)

    # 조합해서 만들 수 있는 숫자
    comb_list = []
    for i in range(1, len(num_list) + 1):
        for j in permutations(num_list, i):
            comb_list.append(int("".join(j)))

    # print(comb_list)

    # 소수 개수 세기
    answer = 0
    for num in set(comb_list):  # 중복 숫자 제거
        if num < 2:
            continue

        ok = True
        for x in range(2, num):
            # 소수가 아니면
            if num % x == 0:
                ok = False
                break

        # 소수이면 카운트 업
        if ok:
            answer += 1

    return answer
