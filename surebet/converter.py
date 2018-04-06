# -*- coding: utf-8 -*-
from decimal import Decimal

TWO = Decimal(10) ** -2


def frac_to_dec(numerator: int = 1, detonator: int = 1) -> Decimal:
    """

    :param numerator: int
    :param detonator: int
    :return: dec_odds: Decimal
    """
    dec_odds = Decimal((numerator / detonator) + 1).quantize(TWO)
    return dec_odds


def per_to_dec(probability: float = 1) -> Decimal:
    """

    :param probability:
    :return: dec_odds: Decimal
    """
    dec_odds = Decimal(100 / probability).quantize(TWO)
    return dec_odds


def us_to_dec(odds: int = 100) -> Decimal:
    """

    :param odds: int value of American odds positive or negative
    :return: dec_odds: Decimal
    """
    if odds >= 0:
        return Decimal((odds / 100) + 1).quantize(TWO)
    else:
        return Decimal((100 / odds) + 1).quantize(TWO)
