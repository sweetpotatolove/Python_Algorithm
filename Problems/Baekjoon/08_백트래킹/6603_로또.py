import sys
input = sys.stdin.readline

def rotto(now, cnt):
    if cnt == 6:
        print(' '.join(map(str, answers)))
        return
    
    for idx in range(now, len(N_list)):
        if temp[idx] in answers:
            continue
        answers.append(temp[idx])
        rotto(idx, cnt + 1)
        answers.pop()

def func(now, cnt):
    if cnt == k:
        for t in result:
            temp.append(t)
        rotto(0, 0)
        return
    
    for idx in range(now, len(N_list)):
        if N_list[idx] in result:
            continue
        result.append(N_list[idx])
        func(idx, cnt + 1)
        result.pop()

while True:
    N_list = list(map(int, input().split()))
    if N_list[0] == 0:
        break

    k = N_list.pop(0)
    result = []
    temp = []
    answers = []
    func(0, 0)
    print()
