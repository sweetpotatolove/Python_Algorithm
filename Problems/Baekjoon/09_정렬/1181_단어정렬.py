import sys
input = sys.stdin.readline
N = int(input())
N_list = [input().strip() for _ in range(N)]

l_w = []
for i in N_list:
    if (len(i), i) in l_w:
        continue
    l_w.append((len(i), i))

result = sorted(l_w, key=lambda x : (x[0], x[1]))
for l, p in result:
    print(p)