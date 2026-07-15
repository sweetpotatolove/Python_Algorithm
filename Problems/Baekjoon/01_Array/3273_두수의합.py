import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
cnt = 0
temp = set()
for num1 in numbers:
    num2 = x - num1      
    if num2 in temp:    # 두번째수 돌 때 체크
        cnt += 1
    temp.add(num1)      # 첫번째 수 기록
print(cnt)