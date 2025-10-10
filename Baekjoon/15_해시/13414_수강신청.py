import sys
input = sys.stdin.readline
K, L = map(int, input().split())
student = []
for _ in range(L):
    student.append(input().strip())

select = dict()
for idx, num in enumerate(student):
    select[num] = idx

cnt = 0
for i, j in sorted(select.items(), key=lambda x:x[1]):
    print(i)
    cnt += 1
    if cnt == K:
        break



