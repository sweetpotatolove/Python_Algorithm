import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result = []
answers = set()
def func(now, cnt):
    if cnt == M:
        answers.add(tuple(N_list[p] for p in result))
        return
    
    for idx in range(now, len(N_list)):
        if idx in result:
            continue
        result.append(idx)
        func(idx, cnt + 1)
        result.pop()

func(0, 0)
for seq in sorted(answers):
    print(' '.join(map(str, seq)))