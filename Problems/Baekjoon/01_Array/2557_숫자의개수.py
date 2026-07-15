import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
check = [0] * 10
for i in result:
    check[int(i)] += 1
for j in range(len(check)):
    print(check[j])
