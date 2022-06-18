def fibonacci(n):
    # Input check
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")

    # array declaration
    f = [0] * (n + 1)
 
    # base case assignment
    f[1] = 1
 
    # calculating the fibonacci and storing the values
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = 40 # --> Fibonaci number n
for n in range(1, n + 1):
    print(n, ":", fibonacci(n))
