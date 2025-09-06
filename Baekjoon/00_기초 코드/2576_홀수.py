number_sum = 0
min_number = 100
for _ in range(7):
    num = int(input())
    if num % 2 != 0:    # 홀수라면
        number_sum += num   # 더하기
        min_number = min(min_number, num)

if number_sum > 0:
    print(number_sum)
    print(min_number)
else:
    print(-1)

