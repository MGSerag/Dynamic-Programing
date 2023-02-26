# return the number of pairs that their sum is a full square and for numbers[i] + number[j], (i) >= (j)
import time

def solution(a):
    sums = 0
    for i in a:
        for j in a:
            sums = sums + int("{}{}".format(i, j))

    return sums



a = [10, 2]
t0 = time.time()
print(solution(a))
t1 = time.time()
print(t0-t1)
