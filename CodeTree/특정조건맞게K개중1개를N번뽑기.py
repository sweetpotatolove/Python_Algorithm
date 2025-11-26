
K, N = map(int, input().split())

numbers = set()
def dfs(cnt, num, re, recnt):
    # cnt: 뽑은 개수
    # num: 뽑은 숫자들
    # re: 이전 숫자
    # recnt: 겹친 횟수
    if cnt == N:
        numbers.add(num)
        return

    for i in range(1, K+1):
        # 숫자 뽑는데 이전 숫자와 겹치면
        if re == i:
            # 뽑으면 안되는 경우면
            if recnt:
                recnt = False
                continue
            else:
                dfs(cnt + 1, num + str(i), i, True)

        # 이전 숫자랑 안겹치면
        else:
            dfs(cnt + 1, num + str(i), i, False)

    return

dfs(0, '', 0, False)
# print(sorted(numbers))
for s in sorted(numbers):
    for ss in s:
        print(ss, end=' ')
    print()