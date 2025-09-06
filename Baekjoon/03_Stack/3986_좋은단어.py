import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    word = input().strip()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        cnt += 1

print(cnt)