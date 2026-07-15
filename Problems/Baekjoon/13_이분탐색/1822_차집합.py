import sys
input = sys.stdin.readline
na, nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
AnotB = []
sB = set(B)
for i in A:
    if i not in sB:
        AnotB.append(i)

AnotB_sort = sorted(AnotB)
print(len(AnotB_sort))
print(*AnotB_sort)
