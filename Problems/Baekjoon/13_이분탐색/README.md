## 🔹 이분 탐색 (Binary Search) 
⚡ 이분 탐색(Binary Search)은 **정렬된 배열에서 원하는 값을 빠르게 찾는 알고리즘**

⚡ 탐색 범위를 절반씩 줄여가며 시간 복잡도를 `O(log N)`까지 줄이는 것이 특징임

> 🚀 단순한 값 찾기뿐만 아니라, **최적화 문제(최댓값, 최솟값 등)** 에도 자주 사용됩니다!

### 🔍 사용 조건
이분 탐색을 쓰기 위해선 보통 다음 중 하나의 조건을 만족해야 합니다:

- **데이터가 정렬되어 있거나**,  
- **어떤 조건을 만족하는 값의 범위가 연속적일 때**  
  (ex. "x 이상이면 가능, x 미만이면 불가능" 같은 **단조성**)

### 🔁 기본 패턴
1. **정렬된 배열에서 값 찾기 (기본형)**
    ```python
    def binary_search(arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid  # 또는 True
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1  # 또는 False
    ```

2. 조건을 만족하는 최대/최솟값 찾기 (파라메트릭 서치)
    ```python
    # 어떤 mid 값이 조건을 만족하는가?
    def is_possible(mid):
        # 조건 검사
        return True or False

    # 이분 탐색
    start, end = 최소값, 최대값
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if is_possible(mid):
            result = mid        # 또는 조건에 따라 갱신
            start = mid + 1     # 더 큰 값 시도
        else:
            end = mid - 1       # 더 작은 값 시도

    print(result)
    ```

### ✅ 예시 문제: 과자 나눠주기 (백준 16401)
- 문제 설명
  - N개의 과자를 M명의 조카에게 같은 길이로 나눠주되, 잘라도 되지만 합치는 건 불가능
  - 조카 한 명당 과자 하나씩만 주되, 가능한 가장 긴 길이로 나눠주기
  - 목표: 가능한 과자 길이의 최댓값

- 적용 방식
  - 가능한 과자 길이를 `1 ~ max(과자 길이)` 사이로 두고 이분 탐색
  - 어떤 길이 `mid`로 자르면 조카 수 이상 줄 수 있는지 체크

- 코드
  ```python
  def can_distribute(length):
      return sum(s // length for s in snacks) >= M

  start, end = 1, max(snacks)
  result = 0

  while start <= end:
      mid = (start + end) // 2

      if can_distribute(mid):
          result = mid
          start = mid + 1
      else:
          end = mid - 1

  print(result)
  ```

### ⚙️ 시간 복잡도
탐색 범위를 절반씩 줄이므로 `O(log N)`

※ 단, `is_possible()` 안에서 매번 선형탐색을 한다면 → `O(N log N)`

### 🧠 Tip!!
- `mid = (start + end) // 2`는 항상 정수 (소수점 안 나옴)
- 무한 루프 방지를 위해 `start <= end` 조건에 유의
- 파라메트릭 서치의 핵심은 조건을 만족하는지의 여부만 판단하면 됨


## 🔹 리스트 vs 집합(set)
⚡ Python에서 데이터를 탐색할 때 많이 사용하는 자료구조는 `list`와 `set`

⚡ 두 자료구조는 **`in` 연산자(포함 여부 검사)**에서 성능 차이가 큼

### 🔍 list와 set 핵심 비교
| 항목 | 리스트 (`list`) | 집합 (`set`) |
|------|------------------|---------------|
| 중복 허용 | O | ❌ (자동 제거) |
| 순서 유지 | O | ❌ |
| 탐색 속도 (`in` 연산) | **O(N)** | **O(1)** (평균) |
| 내부 구조 | 배열 기반 | 해시 테이블 기반 |
| 적합한 상황 | 순서 중요, 소량 데이터 | 빠른 탐색, 대량 데이터 |

### ✅ 예시 문제: 숫자 카드 (백준 10815)
- 문제 설명
  - 상근이는 숫자 카드 `N`개를 가지고 있음
  - `M`개의 수가 주어질 때, 상근이가 그 수를 가지고 있는지 판별
  - N, M ≤ 500,000 (데이터 많음)

- ❌ 리스트 사용 (비효율적)
  ```python
  cards = list(map(int, input().split()))
  for num in numbers:
      if num in cards:
          print(1, end=' ')
      else:
          print(0, end=' ')
  ```
  - 리스트는 `in` 연산 시 앞에서부터 순차 탐색
  - 시간복잡도: `O(N × M)` → 입력이 많으면 시간 초과

- ✅ 집합(set) 사용 (효율적)
  ```python
  cards = set(map(int, input().split()))
  for num in numbers:
      if num in cards:
          print(1, end=' ')
      else:
          print(0, end=' ')
  ```
  - 집합은 내부적으로 **해시 테이블**을 사용
  - 시간복잡도: `O(N + M)` → 매우 빠름

- 속도 비교
  | 데이터 수    | 리스트 사용   | 집합 사용  |
  | -------- | -------- | ------ |
  | 100,000개 | 약 1~2초   | < 0.1초 |
  | 500,000개 | 시간 초과 발생 | 정상 수행  |

### 🧠 결론
- **데이터 존재 여부만 빠르게 확인**하고 싶을 땐 무조건 `set`을 쓰자
- `list`는 순서가 필요하거나, 작은 데이터 처리에 적합
- 특히 입력 데이터가 크고 `in` 연산을 반복하는 경우는 set이 필수


## 🔹 상대 순위 (Rank) 변환
⚡ 상대 순위(Ranking) 는 값의 "서열 관계"만 유지하고 싶을 때 사용되는 테크닉

즉, 값의 크기 자체가 아니라 크기의 상대적 순서만 중요할 때 유용함

### 🔍 개념
리스트 안의 각 원소를 "해당 값이 전체에서 몇 번째로 작은지(=순위)"로 변환

-> **중복값은 같은 순위**를 가지게 됨

### 🔁 기본 패턴
```python
data = [12, 5, 5, 20]
```

1️⃣ 중복 제거 후 정렬
```python
sorted_unique = sorted(set(data))  # [5, 12, 20]
```

2️⃣ 각 값 → 순위 매핑
```python
rank = {v: i for i, v in enumerate(sorted_unique)}
# {5: 0, 12: 1, 20: 2}
```

3️⃣ 순위 변환
```python
ranks = [rank[x] for x in data]
# [1, 0, 0, 2]
```

### ✅ 예시 문제: 멀티버스2 (백준 18869)
- M개의 우주가 있고, 각 우주에는 N개의 행성이 있음
- 각 행성은 고유한 크기를 가지지만, 우주마다 크기의 절대값은 다를 수 있음
- "서열(크기 비교 관계)"만 같으면 두 우주는 같은 구조의 우주로 간주
```python
M, N = map(int, input().split())
universes = []

for _ in range(M):
    data = list(map(int, input().split()))
    sorted_unique = sorted(set(data))
    rank = {v: i for i, v in enumerate(sorted_unique)}
    universes.append(tuple(rank[x] for x in data))

print(universes)
# [(1,2,0,1), (1,2,0,1), (0,1,2,0)]
```
- 같은 (1,2,0,1) 패턴이면 "같은 우주"로 간주할 수 있음

### ⚙️ 시간 복잡도
- 정렬: `O(N log N)`
- 변환: `O(N)`
- 총 `O(N log N)`


## 🔹 Counter (빈도수 세기)
⚡ `collections.Counter` 는 데이터의 **등장 횟수를 손쉽게 세는 클래스형 자료구조**

-> 딕셔너리와 비슷하지만, "값의 빈도수"에 특화됨

### 🔍 기본 사용법
```python
from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(data)
print(count)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})
```
- `count['apple']` -> 3
- 가장 많이 등장한 항목: `count.most_common(1)` -> `[('apple', 3)]`

### ✅ 예시 문제: 멀티버스2 (백준 18869)
```python
from collections import Counter

# 상대 순위로 변환된 각 우주
universes = [
    (1, 2, 0, 1),
    (1, 2, 0, 1),
    (0, 1, 2, 0)
]

cnt = Counter(universes)
print(cnt)
# Counter({(1, 2, 0, 1): 2, (0, 1, 2, 0): 1})

# 같은 패턴의 쌍 개수 = nC2 = v*(v-1)//2
result = sum(v * (v - 1) // 2 for v in cnt.values())
print(result)  # 1
```
- ➡️ `(1,2,0,1)` 패턴이 2번 등장 -> 쌍 1개 (2C2 = 1)
- ➡️ `(0,1,2,0)` 패턴은 1번 등장 -> 쌍 없음

### ⚙️ 시간 복잡도
- Counter 생성: `O(N)`
- 빈도 계산 및 조합 합산: `O(N)`
- 전체 O(N)

