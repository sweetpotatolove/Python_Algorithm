num1, num2, num3 = map(int, input().split())

if num1 == num2:
    if num2 == num3:    # num1 == num2 == num3
        print(10000 + num1 * 1000)
    else:   # num1 == num2 != num3
        print(1000 + num1 * 100)
elif num1 == num3:  # num1 == num3 != num2
    print(1000 + num1 * 100)
elif num2 == num3:
    print(1000 + num2 * 100)
else:   # num1 != num2 != num3
    print(max(num1, num2, num3) * 100)