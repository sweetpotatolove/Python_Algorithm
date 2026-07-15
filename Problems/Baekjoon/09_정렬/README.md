# 📚 Python 정렬 함수 정리
⚡ 파이썬의 정렬은 Timsort 알고리즘(O(N log N))을 사용함

### 🔹 `sorted()`
- **iterable**(리스트, 문자열, 튜플 등)을 정렬하여 **새로운 리스트 반환**
- 원본은 그대로 유지
```python
nums = [5, 2, 9, 1]
print(sorted(nums))                 # [1, 2, 5, 9]
print(nums)                         # [5, 2, 9, 1] (원본 유지)
```

### 주요 옵션
```python
words = ["banana", "apple", "cherry"]

print(sorted(words))                           # 기본 오름차순
print(sorted(words, reverse=True))             # 내림차순
print(sorted(words, key=len))                  # 길이 기준 정렬
print(sorted(words, key=lambda x: (len(x), x)))# 길이 → 사전순 다중 기준
```

### 🔹 `.sort()`
- **리스트 전용 메서드**
- 리스트를 **제자리(in-place)에서 정렬**
- 반환값은 `None`
```python
nums = [5, 2, 9, 1]
nums.sort()
print(nums)   # [1, 2, 5, 9]
```

옵션은 sorted()와 동일함:
```python
words = ["banana", "apple", "cherry"]
words.sort(key=len, reverse=True)
print(words)  # ['banana', 'cherry', 'apple']
```

### 🔹 `reversed()`
- 정렬이 아니라 **순서 뒤집기**
- 결과는 iterator로 반환
```python
nums = [1, 2, 3]
print(list(reversed(nums)))   # [3, 2, 1]
```

## 정렬 함수 활용
### 🔹 기본 정렬
```python
# 오름차순 & 내림차순
nums = [5, 2, 9, 1]
print(sorted(nums))             # [1, 2, 5, 9]
print(sorted(nums, reverse=True)) # [9, 5, 2, 1]
```
※ sorted()는 원본을 보존하고 새 리스트 반환, .sort()는 원본을 정렬하고 None 반환

### 🔹 문자열 정렬
```python
words = ["im", "it", "no", "but", "wait"]

res = sorted(words, key=lambda x: (len(x), x))
print(res)  # ['im', 'it', 'no', 'but', 'wait']
```

### 🔹 숫자 변형 후 정렬
```python
# 숫자를 받아서 자릿수 내림차순으로 재배열 후 리스트 전체 정렬
nums = [321, 45, 908]

res = []
for num in nums:
    new_num = int(''.join(sorted(str(num), reverse=True)))
    res.append(new_num)

res.sort()
print(res)  # [54, 321, 980]
```

### 🔹 절댓값 기준 정렬
```python
nums = [-5, 3, -2, 8]
print(sorted(nums, key=abs))   # [-2, 3, -5, 8]
```

### 🔹 튜플/리스트 정렬
```python
# (길이, 단어) 형태의 튜플을 길이 → 단어 사전순으로 정렬
pairs = [(3, 'but'), (2, 'im'), (2, 'it'), (4, 'wait')]
res = sorted(pairs, key=lambda x: (x[0], x[1]))
print(res)
# [(2, 'im'), (2, 'it'), (3, 'but'), (4, 'wait')]
```
`operator.itemgetter`를 쓰면 더 간단함:
```python
from operator import itemgetter
print(sorted(pairs, key=itemgetter(0, 1)))
```

### 🔹 순서 반전 (reversed)
```python
s = "12345"
print(''.join(reversed(s)))  # '54321'
print(s[::-1])               # '54321' (슬라이싱 활용)
```

