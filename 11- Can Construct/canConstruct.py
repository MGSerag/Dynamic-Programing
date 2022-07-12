memo = {}

def canConstruct(target, wordBank):

    #if targetSum in memo: return memo[targetSum]        
    if target == '': return True

    for word in wordBank:
        if (target.find(word)) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank) == True:
                return True

    return False

target = 'abcdef'
wordBank = ['ab', 'abc', 'cd', 'def', 'abcd']

print(canConstruct(target, wordBank))