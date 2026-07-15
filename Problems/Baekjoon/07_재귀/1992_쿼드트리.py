import sys
input = sys.stdin.readline
N = int(input())
qued = [list(map(str, input().strip())) for _ in range(N)]

def is_same(x, y, size):
    temp = qued[x][y]
    ok = True
    for i in range(x, x+size):
        for j in range(y, y+size):
            if temp != qued[i][j]:
                ok = False
    return ok


def Quad_Tree(x, y, size):
    # 숫자 같으면
    if is_same(x, y, size):
        result.append(qued[x][y])
        return
    
    # 숫자 다르면 쪼개기
    size = size // 2

    # 쪼개지면 괄호 스타트
    result.append('(')
    for i in range(2):
        for j in range(2):
            Quad_Tree(x + i * size, y + j * size, size)
    # 쪼갠거 끝나면 괄호 닫기
    result.append(')')

result = []
Quad_Tree(0, 0, N)
print(''.join(result))