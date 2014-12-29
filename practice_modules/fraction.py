#! /usr/bin/env python

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction(object):
    def __init__(self, top, bottom):
        if not isinstance(top, int) or not isinstance(bottom, int):
            # msg = 'Numerator and Denominator must both be integers'
            raise TypeError()
        self.num = top // gcd(top, bottom)
        self.den = bottom // gcd(top, bottom)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __add__(self, f2):
        num = self.num * f2.den + self.den * f2.num
        den = self.den * f2.den
        # common = gcd(num, den)
        # return Fraction(num//common, den//common)
        return Fraction(num, den)

    def __sub__(self, f2):
        num = self.num * f2.den - self.den * f2.num
        den = self.den * f2.den
        # common = gcd(num, den)
        # return Fraction(num//common, den//common)
        return Fraction(num, den)

    def __mul__(self, f2):
        num = self.num * f2.num
        den = self.den * f2.den
        # common = gcd(num, den)
        # return Fraction(num//common, den//common)
        return Fraction(num, den)

    def __div__(self, f2):
        num = self.num * f2.den
        den = self.den * f2.num
        # common = gcd(num, den)
        # return Fraction(num//common, den//common)
        return Fraction(num, den)

    def __eq__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a == b

    def __ne__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a != b

    def __gt__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a > b

    def __ge__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a >= b

    def __lt__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a < b

    def __le__(self, f2):
        a = self.num * f2.den
        b = self.den * f2.num
        return a <= b

if __name__ == '__main__':
    x = Fraction(2, -16)
    y = Fraction(1, 4)
    print(x)
    x += y
    print(x)
