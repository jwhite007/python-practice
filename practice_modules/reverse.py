#! /usr/bin/env python


def rev_string_rec(string):
    rev_string = ''
    if len(string) == 1:
        return string + rev_string
    return rev_string_rec(string[1:]) + string[0]


def rev_list(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        return rev_list(my_list[1:]) + my_list[:1]

if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print rev_list(l)
    print rev_string_rec('string')
