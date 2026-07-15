import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().strip().split())))

def is_same(x, y, n):
    ok = True
    temp = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if temp != paper[i][j]:
                ok = False
    return ok

cnt1 = 0    # 파란종이
cnt0 = 0    # 하얀종이
def count(x, y, n):
    global cnt1, cnt0
    if is_same(x, y, n):   # 종이 내용물이 다 같으면 그만
        if paper[x][y] == 1:
            cnt1 += 1
        else:
            cnt0 += 1
        return
    # 종이 내용물 다르면 자르기
    n = n // 2
    for i in range(2):
        for j in range(2):
            count(x + i * n, y + j * n, n)

count(0, 0, N)
print(cnt0)
print(cnt1)