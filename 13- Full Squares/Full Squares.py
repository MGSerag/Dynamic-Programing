# return the number of pairs that their sum is a full square and for numbers[i] + number[j], (i) >= (j)

def solution(numbers):
    # n = 0
    sums = [ x + y for i, x in enumerate(numbers) for j, y in enumerate(numbers) if i >= j and x + y >= 0 
    and (int((x+y)**0.5 + 0.5) ** 2 == (x+y) or (x+y) == 0)]
    # full_squares = [x for x in sums if int(x**0.5 + 0.5) ** 2 == x or x == 0]
    return len(sums)
    # n = sum(map(lambda x : int(x**0.5 + 0.5) ** 2 == x or x == 0, sums))
    # for num_sum in sums:
    #         # root = num_sum ** 0.5
    #         if int(num_sum ** 0.5 + 0.5) ** 2 == num_sum:
    #             n = n + 1

    # for i in range(len(numbers)):
    #     for j in range(i, len(numbers)):
    #         num_sum = numbers[i] + numbers[j]
    #         if num_sum < 0:
    #             continue
                
    #         print(i, j, num_sum)
    #         root = num_sum ** 0.5
    #         if int(root + 0.5) ** 2 == num_sum:
    #             n = n + 1
                
    # return n