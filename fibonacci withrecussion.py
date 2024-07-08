def fib(n):
    fib_seq=[0,1]

    if n<=1:
        return fib[:n+1]
    else:
        for i in range(2,n+1):
            next=fib(-1)+fib(-2)
            fib(next)
        return fib
n=10
print("fib sequence")
print(fib(n))
        
