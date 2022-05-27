from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    # Input check
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")

    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-1)

n = 400 # --> Fibonaci number n
for n in range(1, n + 1):
    print(n, ":", fibonacci(n))