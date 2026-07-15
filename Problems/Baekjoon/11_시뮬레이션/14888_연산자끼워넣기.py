def dfs(index, current, add, sub, mul, div):
    global max_value, min_value
    
    # 모든 수를 다 사용했으면 결과 갱신
    if index == N:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return
    
    # 덧셈
    if add > 0:
        dfs(index + 1, current + numbers[index], add - 1, sub, mul, div)
    # 뺄셈
    if sub > 0:
        dfs(index + 1, current - numbers[index], add, sub - 1, mul, div)
    # 곱셈
    if mul > 0:
        dfs(index + 1, current * numbers[index], add, sub, mul - 1, div)
    # 나눗셈
    if div > 0:
        if current < 0:
            dfs(index + 1, -(-current // numbers[index]), add, sub, mul, div - 1)
        else:
            dfs(index + 1, current // numbers[index], add, sub, mul, div - 1)


N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -10**9
min_value = 10**9

dfs(1, numbers[0], add, sub, mul, div)

print(max_value)
print(min_value)
