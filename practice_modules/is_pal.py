#! /usr/bin/env python


def is_pal(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    parsed_string = ''
    for i in string:
        if i in letters:
            parsed_string = parsed_string + i
    for i in range(len(parsed_string)//2):
        if parsed_string[i] != parsed_string[-(i + 1)]:
            return False
    return True

def is_pal2(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    parsed_string = ''
    for i in string:
        if i in letters:
            parsed_string = parsed_string + i
    i = 0
    j = len(parsed_string) - 1
    pal = True
    while pal:
        if i == j or i > j:
            break
        if parsed_string[i] != parsed_string[j]:
            pal = False
        i += 1
        j -= 1
    return pal

def is_pal3(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    parsed_string = ''
    for i in string:
        if i in letters:
            parsed_string = parsed_string + i
    for i, j in zip(parsed_string[:len(parsed_string) // 2],
                    parsed_string[len(parsed_string) :
                                  len(parsed_string) // 2 - 1 : -1]):
        if i != j:
            return False

    return True

if __name__ == '__main__':
    str1 = 'mom'
    str2 = 'ink'
    str3 = 'thissiht'
    str4 = "Madam, I'm Adam"
    str5 = 'In girum imus nocte et consumimur igni'
    print is_pal3(str1)
    print is_pal3(str2)
    print is_pal3(str3)
    print is_pal3(str4)
    print is_pal3(str5)
    # from timeit import timeit
    # print timeit(stmt='is_pal(str5)', setup='from __main__ import is_pal, str5')
    # print timeit(stmt='is_pal2(str5)', setup='from __main__ import is_pal2, str5')
