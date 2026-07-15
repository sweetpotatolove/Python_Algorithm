N, X = map(int, input().split())
N_list = list(map(int, input().split()))
for i in N_list:
    if X > i:
        print(i, end=' ')