def shell(n):
    return [[0 for x in range(min(idx + 1, 2 * n - idx - 1))] for y, idx in enumerate(range(2 * n - 1))]

n = 5
print(shell(n))
