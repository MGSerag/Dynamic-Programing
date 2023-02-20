# Take a string and search through prefixed.
# Take out the longes pliandrome prefix and return remaining string
# if prefix is on char return string

def solution(s):
    longest = 0
    for i in range(len(s)+1):
        
        x = s[:i]
        # print(i, x)
        if x == x[::-1]:
            longest = i
    
    print(s, longest < 2)
    if longest < 2:
        if s == None:
            return ""
        return s
    else:
        return(solution(s[longest:]))
    
    # print(s[longest:])

s="abbab"
# print(s[4:])
print(solution(s))
    
