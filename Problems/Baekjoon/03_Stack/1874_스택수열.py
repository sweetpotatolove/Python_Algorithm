import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

check = 1
stack = []
result = []
ok = True
for num in numbers:
    while check <= num:
        # 그 숫자까지 스택에 넣기
        stack.append(check)
        check += 1
        result.append('+')
    
    # 뺄 수 있는 숫자인지 확인
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        ok = False

if ok:
    # 문제 없었으면 출력
    for i in result:
        print(i)
else:
    print("NO")
    