import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().strip().split())))

def same(x, y, size):
    temp = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if temp != paper[i][j]:
                return False
    return True

cnt0 = 0    # 0 카운트
cnt1 = 0    # 1 카운트
cnt_1 = 0   # -1 카운트

def count(x, y, size):
    global cnt0, cnt1, cnt_1
    if same(x, y, size):    # 종료조건: 해당 범위 종이가 다 같은 종류면
        if paper[x][y] == 1:
            cnt1 += 1
        elif paper[x][y] == 0:
            cnt0 += 1
        else:
            cnt_1 += 1  
        return
    
    size = size // 3
    for i in range(3):
        for j in range(3):
            count(x + i * size, y + j * size, size)

count(0, 0, N)
print(cnt_1)
print(cnt0)
print(cnt1)