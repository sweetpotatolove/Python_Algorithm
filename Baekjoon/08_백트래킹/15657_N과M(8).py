import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result = []
def func(now, cnt):
    if cnt == M:
        print(' '.join(result))
        return
    for idx in range(now, len(N_list)):
        result.append(f'{N_list[idx]}')
        func(idx, cnt + 1)
        result.pop()

func(0, 0)