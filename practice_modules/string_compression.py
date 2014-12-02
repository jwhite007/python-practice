#! /usr/bin/env python


def compr_str(string):
    compr_str = ''
    count = 0
    # import pdb; pdb.set_trace()
    for i in string:
        if compr_str == '':
            compr_str = i
            count += 1
        elif compr_str[len(compr_str) - 1] == i:
            count += 1
        else:
            compr_str = compr_str + str(count) + i
            count = 1
    compr_str = compr_str + str(count)
    if len(compr_str) == len(string) * 2:
        return string
    else:
        return compr_str


if __name__ == '__main__':
    print compr_str('aabbbcccc')
    print compr_str('aabbbccccddddd')
    print compr_str('abcd')
