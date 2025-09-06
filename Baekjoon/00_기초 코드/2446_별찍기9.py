import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    print(' '*i + '*'*(N*2-i*2-1))

for i in range(1,N):
    print(' '*(N-i-1) + '*'*(i*2+1))
    
