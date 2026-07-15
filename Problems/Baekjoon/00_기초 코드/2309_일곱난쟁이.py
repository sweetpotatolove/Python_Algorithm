people = []
for _ in range(9):
    people.append(int(input()))

ok = False
for i in range(len(people)-1):
    for j in range(i+1, len(people)):
        if (sum(people) - people[i] - people[j]) == 100:
            people.pop(j)
            people.pop(i)
            ok = True
            break
    if ok:
        break

for k in sorted(people):
    print(k)