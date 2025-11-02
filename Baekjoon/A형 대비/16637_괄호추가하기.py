import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
numbers = list(input().strip())
ok = [False] * N
maxnum = -2**31
def calculation(x, cal, y):
    if cal == '+':
        return x + y
    elif cal == '-':
        return x - y
    else:
        return x * y

def dfs(idx):
    global maxnum
    # 괄호를 여는 경우
    if idx <= N - 3:
        ok[idx] = True
        dfs(idx+4)
        ok[idx] = False

    # 괄호를 안여는 경우
    if idx + 2 <= N:
        dfs(idx + 2)
    
    # 계산
    if idx >= N-1:
        temp = []
        i = 0
        # 괄호 연산
        while i < N:
            if i + 2 < N and ok[i] == True:
                result = calculation(int(numbers[i]), numbers[i+1], int(numbers[i+2]))
                temp.append(str(result))
                i += 3
            else: # ok == False:
                temp.append(numbers[i])
                i += 1
        
        # 괄호 연산 후 전체 연산
        i = 0
        result = int(temp[i])
        while i+1 < len(temp):
            result = calculation(result, temp[i+1], int(temp[i+2]))
            i += 2
        
        maxnum = max(maxnum, result)
 
dfs(0)
print(maxnum)