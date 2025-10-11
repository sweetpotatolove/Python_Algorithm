import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        c, t = input().strip().split()
        if t not in clothes:
            clothes[t] = [c]
        else:
            clothes[t].append(c)
    
    result = 1
    for t in clothes:
        # 해당 종류 옷 하나씩 골라입는 경우 + 그 종류 옷 안입는 경우(1)
        result *= (len(clothes[t]) + 1)
    result -= 1     # 모든 종류 안입는 경우의 수 없애기
    print(result)