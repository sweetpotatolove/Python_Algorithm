n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
box = {}
# Please write your code here.
for e1, e2 in edges:
    if e1 in box: # 박스에 있으면
        box[e1].append(e2)
    else:
        box[e1] = [e2]
    if e2 in box: # 박스에 있으면
        box[e2].append(e1)
    else:
        box[e2] = [e1]

ok = False
visited = [False] * n
def dfs(key, cnt):
    global ok
    if cnt == 5:
        ok = True
        return
    
    for v in box[key]:
        if visited[v]:
            continue
        visited[v] = True
        dfs(v, cnt + 1)
        visited[v] = False
    
    return

for k in box.keys():
    visited[k] = True
    dfs(k, 1)
    visited[k] = False
    if ok:
        break

if ok:
    print(1)
else:
    print(0)



