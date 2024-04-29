num = int(input())
order = len(str(num))
sum = 0
temp = num

while temp>0:
    digit = temp % 10
    cube = digit ** order
    sum += cube
    temp //= 10

if sum == num:
    print("armstrong number")
else:
    print("not armstrong number")
