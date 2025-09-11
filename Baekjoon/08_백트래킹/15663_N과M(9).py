import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
# N_list.sort()

result = []
total = set()
def func(now, cnt):
    temp = []
    if cnt == M:
        for p in result:
            temp.append(N_list[p])
        temp = tuple(temp)
        total.add(temp)
        return
    for idx in range(now, len(N_list)):
        if idx in result:
            continue
        # result.append(f'{N_list[idx]}')
        result.append(idx)
        func(idx, cnt + 1)
        result.pop()

func(0, 0)
print(total.sorted())