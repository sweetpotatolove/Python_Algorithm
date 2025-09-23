import sys
from collections import deque
input = sys.stdin.readline
n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = deque()

# 첫번째 트럭 출발
time = 0
number = 0
current_w = 0
while True:
    time += 1

    # 다리 다 건넜으면 그 트럭 없애기
    if bridge:
        if time - bridge[0][1] == w:
            tr, tt =  bridge.popleft()
            current_w -= tr     # 다리 위 트럭 무게 수정

    # 뒤에 더 보낼 트럭이 있다면
    if number < n:
        # 다리 위의 트럭 무게 + 다음 트럭 무게와 최대 하중 비교
        if current_w + truck[number] <= l:
            bridge.append((truck[number], time))
            current_w += truck[number]
            number += 1
    
    # 트럭 끝까지 보냈고 다리위에 암것도 없으면 끝
    if number == n and not bridge:
        break

print(time)