import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [x for x in range(1, N+1)]

result = []
def func(cnt):
    if cnt == M:
        print(' '.join(result))
        return
    
    for idx in range(len(N_list)):
        result.append(f'{N_list[idx]}')
        func(cnt + 1)
        result.pop()
        
func(0)