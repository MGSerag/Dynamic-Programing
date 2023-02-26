##You are given an array of non-negative integers numbers.
##You are allowed to choose any number from this array and swap any two digits in it.
##If after the swap operation the number contains leading zeros, they can be omitted and not considered (eg: 010 will be considered just 10).
##Your task is to check whether it is possible to apply the swap operation at most once, so that the elements of the resulting array are strictly increasing.

def solution(numbers):
    result = True
    swapped = False
    if len(numbers) == 1:
        return True
        
    for i in range(1, len(numbers)):
        prev = numbers[i-1]
        current = numbers[i]
        if prev >= current:
            result = False
            if swapped:
                return False
            else:
                if i == 1:
                    current = list(str(current))
                    for j in range(len(current)):
                        current[j], current[j-1] = current[j-1], current[j]
                        if prev < int("".join(current)):
                            result = True
                            swapped = True
                            break
                            
                    prev = list(str(prev))
                    for j in range(len(prev)):
                        prev[j], prev[j-1] = prev[j-1], prev[j]
                        if int("".join(prev)) < numbers[i]:
                            result = True
                            swapped = True
                            break
                        

                elif i > 1 and i < len(numbers):
                    current = list(str(current))
                    for j in range(len(current)):
                        current[j], current[j-1] = current[j-1], current[j]
                        if prev < int("".join(current)):
                            result = True
                            swapped = True
                            break    
                    
                    prev = list(str(prev))
                    for j in range(len(prev)):
                        prev[j], prev[j-1] = prev[j-1], prev[j]
                        if numbers[i-2] < int("".join(prev)) < numbers[i]:
                            result = True
                            swapped = True
                            break
                        
                                        
                else:
                    current = list(str(current))
                    for j in range(len(current)):
                        current[j], current[j-1] = current[j-1], current[j]
                        if prev < int("".join(current)) < numbers[i+1]:
                            result = True
                            swapped = True
                            break    
                    
                    prev = list(str(prev))
                    for j in range(len(prev)):
                        prev[j], prev[j-1] = prev[j-1], prev[j]
                        if numbers[i-2] < int("".join(prev)) < numbers[i]:
                            result = True
                            swapped = True
                            break
                            
    return result
