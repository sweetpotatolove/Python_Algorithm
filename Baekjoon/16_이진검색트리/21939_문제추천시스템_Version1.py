import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_heap = []   # (-L, -P)
min_heap = []   # (L, P)
problem_level = dict()

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    problem_level[P] = L

def add(P, L):
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    problem_level[P] = L

def recommend(x):
    if x == 1:
        while max_heap:
            L, P = -max_heap[0][0], -max_heap[0][1]
            if problem_level.get(P) == L:
                print(P)
                return
            heapq.heappop(max_heap)
    else:
        while min_heap:
            L, P = min_heap[0]
            if problem_level.get(P) == L:
                print(P)
                return
            heapq.heappop(min_heap)

def solved(P):
    problem_level.pop(P)

M = int(input())
for _ in range(M):
    temp = input().split()
    cmd = temp[0]
    if cmd == "recommend":
        recommend(int(temp[1]))
    elif cmd == "add":
        add(int(temp[1]), int(temp[2]))
    elif cmd == "solved":
        solved(int(temp[1]))


""" 시간초과
import sys
input = sys.stdin.readline
N = int(input())
problem = dict()
problem_level = dict()
r = []
ok = True
for _ in range(N):
    P, L = map(int, input().split())
    if L not in problem:
        problem[L] = set()
    problem[L].add(P)
    problem_level[P] = L

def add(P, L):
    if L not in problem:
        problem[L] = set()
    problem[L].add(P)
    problem_level[P] = L

def recommend(x):
    if x == 1:
        max_key = max(problem.keys()) # -> 모든 난이도 키 순회
        print(max(problem[max_key]))  # recommend 명령 많으면 O(M*K) -> 시간초과
    else:
        min_key = min(problem.keys())
        print(min(problem[min_key]))   

def solved(p):
    L = problem_level.pop(p)
    problem[L].remove(p)
    if not problem[L]:
        problem.pop(L)

M = int(input())
for _ in range(M):
    temp = list(map(str, input().strip().split()))
    if temp[0] == "recommend":
        recommend(int(temp[1]))
    elif temp[0] == "add":
        add(int(temp[1]), int(temp[2]))
    elif temp[0] == "solved":
        solved(int(temp[1]))
"""