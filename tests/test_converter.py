#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `converter` package."""

from pytest import approx

from decimal import Decimal

from surebet import converter


def test_frac_to_dec():
    assert converter.frac_to_dec(numerator=36, detonator=5) == approx(Decimal(8.20))


def test_pro_to_dec():
    assert converter.pro_to_dec(probability=68) == approx(Decimal(1.47))


def test_us_to_dec():
    assert converter.us_to_dec(odds=205) == approx(Decimal(3.05))
    assert converter.us_to_dec(odds=-200) == approx(Decimal(1.50))


def test_mal_to_dec():
    assert converter.mal_to_dec(odds=0.87) == approx(Decimal(1.87))
    assert converter.mal_to_dec(odds=-.60) == approx(Decimal(2.67))


def test_hk_to_dec():
    assert converter.hk_to_dec(odds=0.87) == approx(Decimal(1.87))


def test_ind_to_dec():
    assert converter.ind_to_dec(odds=5.21) == approx(Decimal(6.21))
    assert converter.ind_to_dec(odds=-2.60) == approx(Decimal(1.38))
