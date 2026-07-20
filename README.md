# Python_Algorithm
파이썬(Python)으로 풀어본 알고리즘 문제 풀이 모음입니다.  
프로그래머스, JUNGOL, SEWA 등 다양한 알고리즘 문제를 연습하며 문제 해결 능력 향상을 목표로 합니다.

각 문제는 문제 유형별로 폴더로 정리되어 있습니다.

## 바로가기

| 주제 | 바로가기 | 포함 내용 |
| --- | --- | --- |
| 기초 | [Baekjoon](Problems/Baekjoon/00_기초%20코드) | 입출력, 조건문, 반복문, 함수, 문자열 처리 |
| 배열/자료구조 | [Baekjoon](Problems/Baekjoon/01_Array) | 배열, 리스트, 집합, 맵/딕셔너리, 정렬 |
| 탐색 | [Programmers](Problems/Programmers/탐색) / [Baekjoon](Problems/Baekjoon/06_BFS)| 완전탐색, BFS, DFS, 백트래킹 |
| 그래프 | [Baekjoon](Problems/Baekjoon) | 그래프 이론, 최단경로, 서로소집합, 위상정렬 |
| 동적계획법 | [Baekjoon](Problems/Baekjoon/10_DP) | DP, 메모이제이션, 타뷸레이션, LIS, 배낭문제 |
| 그리디 | [Baekjoon](Problems/Baekjoon/12_그리디) | 그리디, 우선순위, 정렬 기반 선택 |
| 이분탐색 | [Baekjoon](Problems/Baekjoon/13_이분탐색) | 이분탐색, parametric search |
| 투포인터/슬라이딩윈도우 | [Baekjoon](Problems/Baekjoon/14_투포인터) | 투포인터, 슬라이딩 윈도우 |
| 스택/큐/덱 | [Programmers](Problems/Programmers/스택_큐_덱) / [Baekjoon](Problems/Baekjoon/03_Stack) | 스택, 큐, 덱 |
| 시뮬레이션 | [Baekjoon](Problems/Baekjoon/11_시뮬레이션) | 구현, 시뮬레이션, 수학적 구현 |
| 문자열/해시 | [Baekjoon](Problems/Baekjoon/15_해시) | 문자열, 해시, 카운팅 |
| 트리/힙 | [Baekjoon](Problems/Baekjoon/16_이진검색트리) | 트리, 이진검색트리, 힙/우선순위큐 |


## 📁 폴더 구조
```
Python_Algorithm/
├── Problems/
│   ├── BOJ/
│   │   ├── BFS/
│   │   │   ├── 1926.py
│   │   │   └── ...
│   │   ├── DFS/
│   │   │   ├── 2667.py
│   │   │   └── ...
│   │   └── ...
│   ├── SEWA/
│   │   ├── 구현/
│   │   │   ├── 001.py
│   │   │   └── ...
│   │   └── ...
│   └── ...   
├── Algorithm/
│   └── 알고리즘 개념 정리 (예정)
└── README.md
```

### 파일 이름 규칙

```text
난이도/문제번호_문제이름.py
```

예시:

```text
silver/1997_TigerEatingRiceCakes.py
gold/1183_CoinVendingMachine.py
gold/1459_NumberSelection.py
gold/2468_Password.py
gold/3337_ShoppingMall.py
platinum/1357_FourNumbersSumZero.py
platinum/1214_Histogram.py
```

## 📌 사용 언어
- Python 3.11
- 기본 문법, 표준 라이브러리 위주로 구현
- 일부 문제는 sys, heapq, collections 등의 라이브러리를 사용

## 🧠 문제 풀이 방향
### 문제 파일 상단 기록

```python
# JUNGOL 0000 문제이름
# 난이도:
# 분류:
# 핵심:
# 시간 복잡도:
# 공간 복잡도:
```

예시:
```
### 1214 히스토그램

- 핵심 관찰: 어떤 막대를 높이로 삼으면, 그 막대보다 낮은 막대가 나오기 전까지 좌우로 확장할 수 있다.
- 접근 방향: stack에 높이가 오름차순이 되도록 인덱스를 저장한다.
- 넓이 계산 시점: 현재 막대가 stack top보다 낮아지면 top 막대의 오른쪽 경계가 현재 위치 바로 전으로 확정된다.
- 너비 계산:
  - stack이 남아 있으면 `i - stack[-1] - 1`
  - stack이 비면 `i`
- 복잡도: 각 막대는 한 번 push되고 한 번 pop되므로 시간 `O(N)`, 공간 `O(N)`이다.

### 1459 숫자고르기

- 핵심 관찰: 위쪽 숫자 `i`에서 아래쪽 숫자 `numbers[i]`로 이동하는 그래프로 볼 수 있다.
- 접근 방향: 각 숫자를 시작점으로 두고, 아래쪽 숫자를 따라가다가 다시 시작점으로 돌아오면 정답에 포함한다.
- 복잡도: `N <= 100`이라 시작점마다 탐색하는 `O(N^2)` 풀이로 충분하다.
```

### 풀이 기록 예시
| 문제 | 난이도 | 분류 | 핵심 |
| --- | --- | --- | --- |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | silver | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다 |
| [1183 동전 자판기](gold/1183_CoinVendingMachine.py) | gold | greedy | 사용하는 동전 수 최대화 문제를 남기는 동전 수 최소화 문제로 바꾼다 |
| [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) | platinum | meet_in_the_middle, hash, counter | `A+B = -(C+D)`로 나누고, `A+B` 합의 빈도수를 Counter에 저장해 센다 |

분류 예시:

```text
sorting
binary_search
two_pointer
meet_in_the_middle
hash
counter
greedy
heap
priority_queue
stack
queue
deque
bfs
dfs
dp
graph
string
geometry
brute_force
bitmask
math
cycle
monotone_stack
```

## 🔗 알고리즘 사이트
- [JUNGOL](https://jungol.co.kr/)
- [프로그래머스](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)
- [SWEA (SW Expert Academy)](https://swexpertacademy.com/)

## ✍️ 기록 목적
- 알고리즘 학습 과정 아카이빙
- 코드 리뷰 및 리팩토링 기록
- 코딩 테스트 준비를 위한 복습용 자료

## ⚙️ 개발자 참고
- IDE: VSCode / PyCharm
- Python 버전: 3.11

## 📌 기타
- 이 저장소는 개인 학습 목적입니다.
- 문제 출처 및 저작권은 각 온라인 저지 플랫폼에 있습니다.
