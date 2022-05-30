def fib():
    last = (0, 1)
    while True:
        yield last[0]
        last = last[0] + last[1], last[0]


n = 6
gen = fib()
#print([next(gen) for _ in range(n)])
print([next(gen) for _ in range(n)][n-1])
