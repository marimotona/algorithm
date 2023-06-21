# abbcbba, ababcbb -> true od = 1 / gunnsuu = *2
# aabbbbc
# aabcc
# ABBv -> 
# ' Nnss'

def check_anagram(s:str) -> bool:
    map = {}
    odd_count = 0

    for char in s:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    for count in map.values():
        if count % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
        
    return True

print(check_anagram('racecar'))  # True
print(check_anagram('appleelppa'))  # False
    

    
        
    

