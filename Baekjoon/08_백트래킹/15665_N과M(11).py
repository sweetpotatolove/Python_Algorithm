import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result = []
answers = set()
def func(cnt):
    if cnt == M:
        answers.add(tuple(N_list[p] for p in result))
        return
    
    for idx in range(len(N_list)):
        result.append(idx)
        func(cnt + 1)
        result.pop()

func(0)
for seq in sorted(answers):
    print(' '.join(map(str, seq)))