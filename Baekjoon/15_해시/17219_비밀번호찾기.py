import sys
input = sys.stdin.readline
N, M = map(int, input().split())
password = dict()
for _ in range(N):
    site, pw = input().strip().split()
    password[site] = pw

for _ in range(M):
    s = input().strip()
    print(password[s])
