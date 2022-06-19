memo = {}

def canSum(targetSum, numbers):

    if targetSum in memo: return memo[targetSum]        
    if targetSum == 0: return True
    if targetSum < 0: return False

    for n in numbers:
        remainder = targetSum - n
        if canSum(remainder, numbers) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

targetSum = 10
numbers = [7, 15]

print(canSum(targetSum, numbers))
