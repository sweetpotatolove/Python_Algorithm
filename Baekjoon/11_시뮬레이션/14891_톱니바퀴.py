import sys
input = sys.stdin.readline
t_list = [input().strip() for _ in range(4)]
K = int(input())    # 회전 횟수
info = []
for _ in range(K):
    info.append(list(map(int, input().split())))


head = [0, 0, 0, 0]   # 12시 방향 체크할거임
for t, d in info:
    # t: 바퀴, d: 방향
    t -= 1
    rotate = [0] * 4    # 어느 방향으로 돌릴지 저장할거임
    rotate[t] = d  

    # 돌리기 시작하는 바퀴 기준 왼쪽으로 가는거
    for i in range(t-1, -1, -1):
        # 왼쪽 바퀴의 2번 인덱스랑
        # 오른쪽 바퀴의 6번 인덱스랑 비교
        right = (head[i+1] + 6) % 8
        left = (head[i] + 2) % 8
        if t_list[i][left] != t_list[i+1][right]:
            rotate[i] = -rotate[i+1]
        else:
            break
    
    # 돌리기 시작하는 바퀴 기준 오른쪽으로 가는거
    for j in range(t+1, 4):
        right = (head[j] + 6) % 8
        left = (head[j-1] + 2) % 8
        if t_list[j-1][left] != t_list[j][right]:
            rotate[j] = -rotate[j-1]
        else:
            break
    
    # 회전시키기
    for z in range(4):
        if rotate[z] != 0:
            head[z] = (head[z] - rotate[z]) % 8

score = 0
for s in range(4):
    if t_list[s][head[s]] == '1':
        score += (2 ** s)

print(score)