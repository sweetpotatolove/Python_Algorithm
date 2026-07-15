
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    '''
    password = []
    cursor = 0
    L = list(map(str, input().strip()))
    for i in L:
        if i == '<':
            if cursor > 0:
                cursor -= 1
        elif i == '>':
            if cursor < len(password):
                cursor += 1
        elif i == '-':
            if cursor > 0:
                cursor -= 1
                password.pop(cursor)
        else:
            password.insert(cursor, i)
            cursor += 1
    print(''.join(password))
    '''

    password = []
    temp = deque()
    L = list(map(str, input().strip()))
    for i in L:
        if i == '<':
            if password:    # 비어있지 않다면
                temp.appendleft(password.pop())  # 뺴서 큐 앞에 삽입
        elif i == '>':
            if temp:
                password.append(temp.popleft())
        elif i == '-':
            if password:    # 비어있지 않다면
                password.pop()  # 마지막꺼 제거
        else:
            password.append(i)
    
    
    print(''.join(password + list(temp)))


        