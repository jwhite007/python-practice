#! /usr/bin/env python
from math import floor, log


def dec_to_bin(dec):
    bin = 0
    while dec > 1:
        lg = int(floor(log(dec, 2)))
        dec = dec - (2**lg)
        bin = bin + 10 ** lg
    if dec == 1:
        bin = bin + 1
    return bin


def dec_to_base(dec, base):
    digits = '0123456789abcdef'
    bin = ''
    while dec > 0:
        bin = digits[(dec % base)] + bin
        dec = dec // base

    return bin


def dec_to_base_rec(dec, base):
    digits = '0123456789abcdef'
    bin = ''
    if dec == 0:
        return bin
    else:
        bin = digits[(dec % base)] + bin
        dec = dec // base
        bin = dec_to_base_rec(dec, base) + bin
    return bin


def dec_to_bin_rec(dec):
    bin = 0
    if dec == 1:
        return bin + 1
    elif dec == 0:
        return bin
    else:
        lg = int(floor(log(dec, 2)))
        bin += 10 ** lg
        dec = dec - (2 ** lg)
        bin += dec_to_bin_rec(dec)
    return bin


if __name__ == '__main__':
    print dec_to_base(100, 8)
