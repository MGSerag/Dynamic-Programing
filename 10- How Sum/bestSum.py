memo = {}

def bestSum(targetSum, numbers):

    if targetSum in memo: return memo[targetSum]        
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for n in numbers:
        remainder = targetSum - n
        remainderCombination = bestSum(remainder, numbers)
        
        if remainderCombination != None:
            combination = remainderCombination.copy()
            combination.append(n)

            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination

targetSum = 15
numbers = [1, 5, 7]

print(bestSum(targetSum, numbers))