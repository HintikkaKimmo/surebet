# -*- coding: utf-8 -*-
from decimal import Decimal

TWO = Decimal(10) ** -2


def frac_to_dec(numerator=1, detonator=1):
    return Decimal((numerator / detonator) + 1).quantize(TWO)


def per_to_dec(probability=1):
    return Decimal(100 / probability).quantize(TWO)


def us_to_dec(odds=100):
    if odds >= 0:
        return Decimal((odds / 100) + 1).quantize(TWO)
    else:
        return Decimal((100 / odds) + 1).quantize(TWO)


def main():
    print(frac_to_dec(numerator=36, detonator=5))
    print(per_to_dec(probability=68))
    print(us_to_dec(odds=205))


if __name__ == '__main__':
    main()
