def fact(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

num = 5
print(fact(num))