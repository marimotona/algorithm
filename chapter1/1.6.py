# aabbcc -> a2b2c2
# aa:cc -> 
# aabbaa -> a2b2a2

def count_alpha(s:str) -> str:
    count = 1
    result = ''

    for i in range(1, len(s)):
        if s[i - 1] == s[i]: # i = 1 / b / a
            count += 1 # count = 1
        else:
            result += (s[i - 1] + str(count))
            count = 1

    result += (s[-1] + str(count))

    return result


print(count_alpha('aabbaa'))
print(count_alpha('aabbc'))
print(count_alpha('aaBC'))