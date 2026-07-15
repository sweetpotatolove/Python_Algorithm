import sys
input = sys.stdin.readline().strip()

if '-' in input:
    sp = list(input.split('-'))
else:
    sp = [input]

numbers = []
for s in sp:
    if '+' in s:
        sp2 = list(map(int, s.split('+')))
        plus = 0
        for num in sp2:
            plus += num
        numbers.append(plus)
    else:
        numbers.append(int(s))

result = 0
for i in range(len(numbers)):
    if i == 0:
        result += numbers[i]
    else:
        result -= numbers[i]

print(result)