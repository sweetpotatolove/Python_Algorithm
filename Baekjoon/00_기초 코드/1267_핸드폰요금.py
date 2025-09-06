N = int(input())
second = list(map(int, input().split()))

Y, M = 0, 0
for i in second:
    Y += ((i // 30) * 10) + 10
    M += ((i // 60) * 15) + 15

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)
