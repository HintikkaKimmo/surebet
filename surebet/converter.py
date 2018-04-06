# -*- coding: utf-8 -*-
from decimal import Decimal

TWO = Decimal(10) ** -2


def frac_to_dec(numerator: int = 1, detonator: int = 1) -> Decimal:
    """

    :param numerator: int
    :param detonator: int
    :return: dec_odds: Decimal odds
    """
    dec_odds = Decimal((numerator / detonator) + 1).quantize(TWO)
    return dec_odds


def pro_to_dec(probability: float = 1.00) -> Decimal:
    """

    :param probability:
    :return: dec_odds: Decimal odds
    """
    dec_odds = Decimal(100 / probability).quantize(TWO)
    return dec_odds


def us_to_dec(odds: int = 100) -> Decimal:
    """

    :param odds: int value of American odds positive or negative
    :return: dec_odds: Decimal odds
    """
    if odds >= 0:
        dec_odds = Decimal((odds / 100) + 1).quantize(TWO)
    else:
        dec_odds = Decimal((100 / abs(odds)) + 1).quantize(TWO)
    return dec_odds


def mal_to_dec(odds: float = 1) -> Decimal:
    """

    :param odds: float value of Malay odds positive or negative
    :return: dec_odds: Decimal odds
    """
    if odds >= 0:
        dec_odds = Decimal(odds + 1).quantize(TWO)
    else:
        dec_odds = Decimal(1 + (1 / abs(odds))).quantize(TWO)
    return dec_odds


def hk_to_dec(odds: float = 1.00) -> Decimal:
    """

    :param odds: float Hong Kong odds
    :return: dec_odds: Decimal odds
    """
    dec_odds = Decimal(odds + 1).quantize(TWO)
    return dec_odds


def ind_to_dec(odds=1.00):
    """

    :param odds: float value of Indonesian odds positive or negative
    :return: dec_odds: Decimal odds
    """
    if odds >= 0:
        dec_odds = Decimal(odds + 1).quantize(TWO)
    else:
        dec_odds = Decimal(1 + (1 / abs(odds))).quantize(TWO)
    return dec_odds


