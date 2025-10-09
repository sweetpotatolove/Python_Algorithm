import sys
input = sys.stdin.readline

N = int(input())
total = list(map(int, input().split()))
total.sort()

count = 0

for i in range(N - 2):
    fix = total[i]
    left = i + 1
    right = N - 1

    if fix > 0:
        break

    while left < right:
        s = fix + total[left] + total[right]

        if s == 0:
            # 같은 값이 여러 개일 수 있음 -> 중복처리
            if total[left] == total[right]:
                # 정렬 했으니 왼, 오 같으면 그 사이의 값들 또한 다 같음
                # 조합 조합 조합 조합
                n = right - left + 1
                count += n * (n - 1) // 2
                break
            else:
                l_count = 1
                r_count = 1
                # 같은 값들 묶어서 카운트
                while left + 1 < right and total[left] == total[left + 1]:
                    l_count += 1
                    left += 1
                while right - 1 > left and total[right] == total[right - 1]:
                    r_count += 1
                    right -= 1
                count += l_count * r_count
                left += 1
                right -= 1
        elif s < 0:
            left += 1
        else:
            right -= 1

print(count)
