import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    print('*'*(i+1)+ ' '*((N-i-1)*2) + '*'*(i+1))
for j in range(1, N):
    print('*'*(N-j)+ ' '*(j*2) + '*'*(N-j))
