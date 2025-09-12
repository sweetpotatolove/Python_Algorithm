import sys
input = sys.stdin.readline
N, C = map(int, input().split())

N_list = list(map(int, input().split()))
order= {}   # {값: [빈도, 등장순서]}
cnt = 1
for i in N_list:
    if i in order:
        order[i][0] += 1
    else:
        order[i] = [0, cnt] 
        cnt += 1
        order[i][0] += 1
        
result = sorted(order, key=lambda x : (-order[x][0], order[x][1]))
for p in result:
    for pp in range(order[p][0]):
        print(f'{p}', end=' ')