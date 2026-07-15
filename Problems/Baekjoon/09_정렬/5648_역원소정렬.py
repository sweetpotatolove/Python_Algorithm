import sys
input = sys.stdin.readline
N, *input_list = map(int, input().split())
while len(input_list) < N:
    input_list += list(map(int, input().split()))

# print(input_list)

result = []
for i in input_list:
    str_change = str(i)
    temp = str_change[::-1]
    result.append(int(temp))

result.sort()
for num in result:
    print(num)
