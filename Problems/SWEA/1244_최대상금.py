def search(k):
    global mx

    current = ''.join(map(str, numbers))

    if (k, current) in visited:
        return

    visited.add((k, current))

    if k == change:
        result = int(''.join(map(str, numbers)))
        mx = max(mx, result)
        return

    for i in range(length):
        for j in range(i + 1, length):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            search(k + 1)
            numbers[j], numbers[i] = numbers[i], numbers[j]


T = int(input())

for tc in range(1, T + 1):
    num, cnt = input().split()
    length = len(num)
    change = int(cnt)
    mx = 0
    visited = set()
    numbers = list(map(int, num))
    search(0)
    print(f'#{tc} {mx}')