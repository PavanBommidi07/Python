lower = int(input())
upper = int(input())

for num in range(lower, upper+1):
    temp = num
    sum = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //= 10
    if sum == num:
        print(num)
