number = []
for _ in range(5):
    number.append(int(input()))

print(int(sum(number)/5))
print(sorted(number)[2])