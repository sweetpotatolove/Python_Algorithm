import sys
input = sys.stdin.readline

# 산성: 양수, 알칼리성: 음수
N = int(input())
total = list(map(int, input().split()))
start = 0
end = len(total) - 1
result = (0, 0)
value = float('inf')
while start < end:
    temp = (total[end] + total[start])

    if abs(temp) < value:   # 0에 더 가깝다면
        value = abs(temp)
        result = (total[start], total[end])

    if temp < 0:
        start += 1
    elif temp == 0:
        print(total[start], total[end])
        break
    else:
        end -= 1

else:
    # while문이 break 없이 끝났을 때
    print(result[0], result[1])