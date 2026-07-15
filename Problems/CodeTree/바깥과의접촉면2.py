from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cnt = 0
ok = False

while True:
    # queue에 숫자 넣기
    numbers = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                numbers.append((i, j))
    
    # 만약 자연수가 없으면 끝 (0 출력)
    if len(numbers) == 0:
        print(0)
        break

    # 숫자 줄이기
    copy = [grid[r][:] for r in range(n)]
    cnt += 1

    while numbers:
        r, c = numbers.popleft()
        zeroCnt = 0
        # 주변에 0 개수 체크
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                zeroCnt += 1

        # 만약 주변에 0 개수가 내 숫자보다 같거나 크면 0으로 바꿈
        if grid[r][c] <= zeroCnt:
            copy[r][c] = 0
        # 그렇지 않으면 개수 빼줌
        else:
            copy[r][c] -= zeroCnt

    # 집합 쪼개져있는지 확인
    visited = [[False] * m for _ in range(n)]
    check = 0
    checkqueue = deque()

    for y in range(n):
        for x in range(m):
            if copy[y][x] == 0 or visited[y][x]:
                continue
            else:
                # 앞에 한번 체크했는데 뭔가 또 걸렸다? 집합 분할돼있다는 뜻
                if check == 1:
                    ok = True
                    print(cnt)
                    break
                checkqueue.append((y, x))
                visited[y][x] = True
                while checkqueue:
                    y_, x_ = checkqueue.popleft()
                    for d in range(4):
                        ny, nx = y_ + dy[d], x_ + dx[d]
                        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and copy[ny][nx] > 0:
                            checkqueue.append((ny, nx))
                            visited[ny][nx] = True
                check += 1
        if ok:
            break

    if ok:
        break

    # 다음 턴 준비
    grid = [copy[r][:] for r in range(n)]
