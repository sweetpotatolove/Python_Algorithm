import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

players = range(N)
min_diff = float('inf')

# 팀을 나누는 모든 조합 생성
for start_team in combinations(players, N // 2):
    link_team = [p for p in players if p not in start_team]
    
    # start 팀 계산
    start_score = 0
    for i, j in combinations(start_team, 2):
        start_score += info[i][j] + info[j][i]
    
    # link 팀 계산
    link_score = 0
    for i, j in combinations(link_team, 2):
        link_score += info[i][j] + info[j][i]
    
    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

    # 차이가 0이면 더 볼 필요 없음
    if min_diff == 0:
        break

print(min_diff)
