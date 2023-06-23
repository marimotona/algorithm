# apple , alepp -> true

def check_string(s1:str, s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    
    map = {}
    for i in range(len(s1)):
        if s1[i] not in map:
            map[s1[i]] = 1
        else:
            map[s1[i]] += 1
    print(map)

    for i in range(len(s2)):
        print(s2[i])
        if s2[i] not in map:
            print(s2[i])
            return False
        
    return True
        
    

# print(check_string('apple', 'alepp'))
# print(check_string('apple', 'appla'))

def check_string2(s1:str, s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    
    new_s1, new_s2 = sorted(s1), sorted(s2)

    for i in range(len(s1)):
        if new_s1[i] != new_s2[i]:
            return False
        
    return True

# print(check_string2('apple', 'alepp'))
# print(check_string2('apple', 'appla'))

def check_string3(s1:str, s2:str) -> bool:
    if len(s1) != len(s2):
        return False
    
    map = {}
    for i in range(len(s1)):
        if s1[i] not in map:
            map[s1[i]] = 1
        else:
            map[s1[i]] += 1
    
    for i in range(len(s2)):
        if s2[i] not in map:
            return False
        else:
            map[s2[i]] -= 1
            if map[s2[i]] == 0:
                del map[s2[i]]

    return len(map) == 0
    
# print(check_string3('apple', 'alepp'))
# print(check_string3('apple', 'appla'))


def table_string(s1:str, s2:str):
    if len(s1) != len(s2):
        return False
    
    map = {}
    for char in s1:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    for char in s2:
        if char not in map:
            return False
        else:
            map[char] -= 1
            if map[char] < 0:
                return False
            
    return True

print(table_string('apple', 'alepp'))
print(table_string('apple', 'appla'))