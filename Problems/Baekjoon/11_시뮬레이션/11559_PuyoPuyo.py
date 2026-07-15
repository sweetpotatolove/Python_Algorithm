import sys  
from collections import deque
input = sys.stdin.readline
info = [list(map(str, input().strip())) for _ in range(12)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    bomb = []

    for i in range(11, -1, -1):
        if set(info[i]) == {'.'}:   # 점만 있을 때 넘기기
            continue

        # 해당 줄에 뿌요가 있다면 연쇄 가능한지 살펴보기
        for j in range(6):
            if info[i][j] != '.' and visited[i][j] == False:   # 뿌요를 만나면
                temp = info[i][j]   # 뿌요 색 저장해놓고
                queue = deque()
                queue.append((i, j))
                remain = [(i, j)]
                visited[i][j] = True  
                
                while queue:
                    y, x = queue.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < 6 and 0 <= ny < 12 and info[ny][nx] == temp and visited[ny][nx] == False:
                            # 근처에 같은 색 뿌요 있으면 거기로 가기
                            queue.append((ny, nx))
                            remain.append((ny, nx))
                            visited[ny][nx] = True
                if len(remain) >= 4:    # 4개 이상 모였으면
                    bomb.append(remain) 

    if not bomb: # 터질거 없으면 끝내기
        break

    for t in bomb:
        for y, x in t:
            info[y][x] = '.' # 터뜨리기

    # 빈자리 채우기
    for col in range(6):
        stack = deque()
        for row in range(11, -1, -1):
            if info[row][col] != '.':
                stack.append(info[row][col])
        for row in range(11, -1, -1):
            if stack:
                info[row][col] = stack.popleft()
            else:
                info[row][col] = '.'
        
    cnt += 1   # 빈자리 싹 넣었으면 카운트

print(cnt)