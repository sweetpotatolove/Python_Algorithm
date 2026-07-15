card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(10):
    start, end = map(int, input().split())
    start -= 1
    end -= 1

    card = card[:start] + card[start:end+1][::-1] + card[end+1:]
    

for i in card:
    print(i, end=' ')
