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
        # answers.add(' '.join(str(N_list[p]) for p in result))
        # for문 밖으로 빼면 동작 달라짐
            # join 매번 따로 만나면서 반복됨 -> 문자열 안붙음
        # 지금은 for문이 먼저 돌아서 문자열된 후 join
        return
    for idx in range(len(N_list)):
        if idx in result:
            continue
        # result.append(f'{N_list[idx]}')
        result.append(idx)
        func(cnt + 1)
        result.pop()

func(0)
# print('\n'.join(sorted(answers)))

# 튜플은 숫자 기준 사전순으로 정렬됨
for seq in sorted(answers):
    print(' '.join(map(str, seq)))