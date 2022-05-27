fib_dict = {}

def fibonacci(n):
    # Input check
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")
        
    if n in fib_dict:
        return fib_dict[n]

    if n in [1, 2]:
        return 1
    else:
        fib_n = fibonacci(n-1) + fibonacci(n-1)
        fib_dict[n] = fib_n
        return fib_n

n = 100 # --> Fibonaci number n
for n in range(1, n + 1):
    print(n, ":", fibonacci(n))