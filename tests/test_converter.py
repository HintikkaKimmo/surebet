#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `converter` package."""

from pytest import approx

from decimal import Decimal

from surebet import converter


def test_frac_to_dec():
    assert converter.frac_to_dec(numerator=36, detonator=5) == approx(Decimal(8.20))


def test_per_to_dec():
    assert converter.per_to_dec(probability=68) == approx(Decimal(1.47))


def test_us_to_dec():
    assert converter.us_to_dec(odds=205) == approx(Decimal(3.05))
