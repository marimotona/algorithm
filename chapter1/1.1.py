def unique(s:str) -> bool:
    map = {}
    for char in s:
        if char not in map:
            map[char] = 1
        else:
            return False
        
    return True

# print(unique('abcdefg'))
# print(unique('abcdde'))

def none_map(s:str) -> bool:
    if (len(s) > 128): return False

    new_str = sorted(s)
    for i in range(1, len(new_str)):
        print(f'new_str[i]:{new_str[i-1]}, new_str[i+1]:{new_str[i]}')
        if new_str[i - 1] == new_str[i]:
            return False
    return True

print(none_map('abcdefg'))
print(none_map('abcdde'))
