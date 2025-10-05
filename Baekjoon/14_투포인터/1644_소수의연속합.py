import sys
input = sys.stdin.readline
N = int(input())

# 시간초과 안나게 소수 구하는 방법: 에라토스테네스의 체
def get_primes(n):
    is_prime = [True] * (n + 1)  # 소수 여부 저장하는 배열
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수 X
    for i in range(2, int(n ** 0.5) + 1):  # 2부터 √n까지 반복
        if is_prime[i]:  # i가 소수면
            for j in range(i * i, n + 1, i):  # # i의 배수들은 전부 소수가 아님
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

def count_prime_sums(n):
    primes = get_primes(n)  # 소수 리스트
    count = 0  # 경우의 수 카운트
    start = end = 0  # 투포인터
    current_sum = 0  # 현재 부분합

    while True:
        if current_sum >= n:
            if current_sum == n:
                count += 1
            current_sum -= primes[start]
            start += 1  # 합 줄이기
        elif end == len(primes):
            break  # 오른쪽 포인터가 끝에 도달하면 종료
        else:
            current_sum += primes[end]
            end += 1  # 합 늘리기
    return count

print(count_prime_sums(N))
