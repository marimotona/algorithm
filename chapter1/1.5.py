# google, googl -> true

def diff_search(s1:str, s2:str) -> bool:
    if len(s1) == len(s2):
        return edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return edit_insert(s1, s2)
    elif len(s1) == len(s2) + 1:
        return edit_insert(s2, s1)

def edit_replace(s1:str, s2:str) -> bool:
    count = 0
    # s1, s2 = sorted(s1), sorted(s2)

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
        if count > 1:
            return False
        
    return True

def edit_insert(s1:str, s2:str) -> bool: # aaabbb, aabbb
    edited = False
    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1

    return True

print(diff_search('pale', 'pal')) # True
print(diff_search('google', 'googler'))
print(diff_search('pale', 'bale'))
print(diff_search('pale', 'bool'))