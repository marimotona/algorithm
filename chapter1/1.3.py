# I am Marimo -> I%20am%20Marimo

def replace(s:str, length:int) -> str:
    replace_word = '%20'

    char_list = list(s)
    print(char_list)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == ' ':
            char_list[new_index - 3 : new_index] = replace_word
            new_index -= 3
            print(char_list)
        else:
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
            print(char_list)

    return ''.join(char_list[new_index:])

    # s = s.replace(' ', replace_word)

    # return s

print(replace('I am Marimo', 11))
# print(replace("much ado about nothing      ", 22))
print(replace(" a b    ", 4))