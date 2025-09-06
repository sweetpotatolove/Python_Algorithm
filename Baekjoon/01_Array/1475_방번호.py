import sys
input = sys.stdin.readline
N = input().strip()
check = [1] * 10
cnt = 1

for i in N:
    if int(i) == 6 and check[6] == 0 and check[9] > 0:
        check[9] -= 1
    elif int(i) == 9 and check[9] == 0 and check[6] > 0:
        check[6] -= 1
    elif check[int(i)] == 0:
        cnt += 1
        check = [x + 1 for x in check]  # 리스트 컴프리헨션
        check[int(i)] -= 1
    else:
        check[int(i)] -= 1
    # print(check)
print(cnt)