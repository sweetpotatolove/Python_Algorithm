num1, num2 = map(int, input().split())
maxnum = max(num1, num2)
minnum = min(num1, num2)
if maxnum - minnum - 1 > 0:
    print(maxnum - minnum - 1)
    for i in range(minnum+1, maxnum):
        print(i, end=' ')

else:
    print(0)