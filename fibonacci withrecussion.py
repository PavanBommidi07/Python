def fib(n):
    fib_seq=[0,1]

    if n<=1:
        return fib_seq[:n+1]
    else:
        for i in range(2,n+1):
            next=fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next)
        return fib_seq
n=10
print("fib sequence")
print(fib(n))
        
