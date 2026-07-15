# 프로그래머스 Lv1. 같은 숫자는 싫어
# 분류: 스택/큐
# 핵심: 연속된 같은 숫자는 한 번만 남기고, 바로 앞 값과 비교하여 중복 제거
# 시간 복잡도: O(n)
# 공간 복잡도: O(n)


# 1. 문제 이해
# - 입력: 숫자 0부터 9까지로 이루어진 정수 배열 arr
# - 출력: 연속적으로 나타나는 숫자를 하나만 남긴 배열
# - 구해야 하는 것: 배열에서 연속적으로 같은 숫자가 이어지는 경우, 그 숫자를 하나만 남기고 나머지는 제거한 결과를 반환하는 함수


# 2. 아이디어
# - 같은 숫자가 연속적으로 나타나는지 여부는 바로 이전 값과 비교하면 판별할 수 있다.
# - 마지막에 넣은 값만 기억하면 되므로 스택처럼 동작하는 방식이 적합하다.
# - 자료구조: 스택 (LIFO)


# 3. 풀이 계획
# 1) answer 리스트에 마지막 원소를 먼저 넣어 기준값을 만든다.
# 2) 남은 원소를 뒤에서부터 하나씩 꺼내며 answer의 마지막 값과 비교한다.
# 3) 같으면 건너뛰고, 다르면 answer에 추가한다.
# 4) 뒤에서부터 꺼냈기 때문에 최종적으로 reverse()를 사용해 원래 순서로 복원한다.


def solution(arr):
    answer = []
    answer.append(arr.pop())

    while (len(arr) > 0):
        num = arr.pop()
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
        
    answer.reverse()

    """
    for num in arr:
        # answer가 비어있거나, 마지막 값이 현재 값과 다르면 넣는다.
        if not answer or answer[-1] != num:
            answer.append(num)
    """
    return answer