def calkin(number):
    def fractions():
        a = b = 1
        while True:
            yield [a, b]
            a, b = b, 2 * (a // b) * b + b - a
            
            
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

# Usage: for calking 1/5, n = [1, 5]. return value is the order of the rational number is Calkin-Wilf tree (0-indexed)
n = [1, 5]
print(calkin(n))
