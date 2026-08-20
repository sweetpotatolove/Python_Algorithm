# 프로그래머스 Lv2. 카펫
# 분류: 완전탐색(약수 탐색)
# 핵심: 노란색 칸의 개수(yellow)는 안쪽 직사각형의 가로*세로와 같으므로, yellow의 약수 쌍을 가로/세로 후보로 탐색하고 테두리(+2)를 더한 전체 칸 수에서 yellow를 뺀 값이 brown과 일치하는지 확인한다.
# 시간 복잡도: O(yellow)
"""
    1. 입력 크기를 정의: 노란색 칸의 개수를 y(yellow)라 하자.
    2. 코드에서 반복문의 실행 횟수를 입력 크기에 대한 함수로 센다.
        -> for yellow_y in range(1, yellow + 1): 정답이 될 조합을 찾을 때까지 최대 yellow번 반복한다.
        -> 반복문 안의 나머지 연산(%), 나눗셈(//), 비교는 모두 O(1)이다.
    3. 따라서 전체 시간 = yellow × O(1) = O(yellow)
"""


# 공간 복잡도: O(1)
"""
    1. 입력 자체를 저장하는 공간은 제외하고, 알고리즘이 추가로 사용하는 메모리만 센다.
    2. 입력 크기에 비례해 커지는 자료구조(리스트, 딕셔너리 등)를 새로 만드는지 확인한다.
        -> 이 코드는 yellow_x, width, height 같은 정수 변수 몇 개만 사용하고 별도의 자료구조를 만들지 않으므로
        -> 추가 공간 = O(1)
"""


# 1. 문제 이해
# - 입력: 카펫에서 갈색 격자의 개수 brown, 노란색 격자의 개수 yellow
# - 출력: 카펫의 가로, 세로 크기 [width, height] (가로가 세로보다 크거나 같음)
# - 구해야 하는 것: 노란색 칸이 이루는 안쪽 직사각형을 감싸는 갈색 테두리(폭 1칸)를 더했을 때, 전체 칸 수에서 노란 칸 수를 뺀 값이 brown과 같아지는 가로/세로 조합


# 2. 아이디어
# - 노란색 칸 개수 yellow는 안쪽 직사각형의 가로*세로와 같으므로, yellow의 약수 쌍(yellow_x, yellow_y)이 안쪽 직사각형의 가로/세로 후보가 된다.
# - 가로가 세로보다 크거나 같다는 조건(yellow_x >= yellow_y)을 만족하는 약수 쌍만 검사해 후보를 줄인다.
# - 안쪽 직사각형에 사방으로 테두리 한 칸씩(각 변에 +2)을 더한 전체 카펫 크기에서 yellow를 뺀 값이 brown과 같은지 확인해, 일치하는 첫 조합을 정답으로 반환한다.


# 3. 풀이 계획
# 1) yellow_y를 1부터 yellow까지 늘려가며 yellow의 약수인지 확인한다(yellow % yellow_y == 0).
# 2) 약수라면 yellow_x = yellow // yellow_y로 가로 길이를 구하고, yellow_x >= yellow_y(가로 >= 세로)를 만족하는지 확인한다.
# 3) 조건을 만족하면 전체 카펫의 width = yellow_x + 2, height = yellow_y + 2를 계산한다.
# 4) width * height - yellow가 brown과 같으면 [width, height]를 반환한다.


def solution(brown, yellow):
    for yellow_y in range(1, yellow + 1):

        # 나누어 떨어지면 가로 길이를 구할 수 있음
        if yellow % yellow_y == 0:
            yellow_x = yellow // yellow_y

            # 가로 >= 세로
            if yellow_x >= yellow_y:
                width = yellow_x + 2
                height = yellow_y + 2

                if width * height - yellow == brown:
                    return [width, height]


# 아래는 시간 초과가 발생한 첫 시도 코드
# 시간 복잡도: O(yellow^2)
"""
    1. 입력 크기를 정의: 노란색 칸의 개수를 y(yellow)라 하자.
    2. 이중 반복문의 실행 횟수를 입력 크기에 대한 함수로 센다.
        -> 바깥 for yellow_y in range(1, yellow + 1)은 최대 yellow번 반복하고,
        -> 안쪽 for yellow_x in range(yellow_y, yellow + 1)도 yellow_y가 작을수록(최악은 1일 때) 거의 yellow번 반복하므로
        -> 전체 반복 횟수는 대략 yellow + (yellow-1) + ... + 1 ≈ yellow^2/2번이다.
        -> 반복문 안의 곱셈(yellow_x * yellow_y), 비교, append는 모두 O(1)이다.
    3. 따라서 전체 시간 = O(yellow^2)
    -> 개선된 코드는 안쪽 반복문을 나머지 연산(%) 한 번으로 대체해 O(yellow)로 줄였다.
"""
"""시간초과
def solution(brown, yellow):
    # 노란색 먼저: 나올 수 있는 경우의 수
    size = []

    for yellow_y in range(1, yellow + 1):
        for yellow_x in range(yellow_y, yellow + 1):
            # 가로(yellow_x)가 세로랑 같거나 더 김
            if yellow_x * yellow_y == yellow:
                size.append((yellow_x, yellow_y))

    # 갈색 확인
    for y_x, y_y in size:
        width = y_x + 2
        height = y_y + 2

        if width * height - yellow == brown:
            return [width, height]
"""