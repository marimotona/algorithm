def match_string(str1:str, str2:str) -> bool:
    isFound = False
    if len(str1) > len(str2):
        i, j = 0, 0
        while len(str1) > i:
            i += 1
            j += 1
            if str1[i] != str2[j]:
                i += 1
                isFound = True

    else:
        i, j = 0, 0
        while len(str2) < j:
            i += 1
            j += 1
            if str1[i] != str2[j]:
                j += 1
                isFound = True

    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                isFound = True

    if isFound:
        return True
    else:
        return False
    

print(match_string('plale', 'plal'))