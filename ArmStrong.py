for i in range(10, 100):
    if i > 2 and i % 2 == 0:
        continue
    count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            if j == 1:
                count += 1 
            else:
                count += 2  
    if count == 2:  
        print(i, end=' ')
