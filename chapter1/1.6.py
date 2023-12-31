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


# string builder

def count_alpha_build(s:str) -> str:
    count = 1
    result = []

    for i in range(1, len(s)):
        if s[i - 1] == s[i]: # i = 1 / b / a
            count += 1 # count = 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1

    result.append(s[-1] + str(count))

    return ''.join(result)

print(count_alpha_build('aabbaa'))
print(count_alpha_build('aabbc'))
print(count_alpha_build('aaBC'))


def alpha_build(s:str) -> str:
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += (s[i - 1] + str(count))
            count = 1

    result += (s[-1] + str(count))

    return result

print(alpha_build('aabbaa'))
print(alpha_build('aabbc'))
print(alpha_build('aaBC'))
