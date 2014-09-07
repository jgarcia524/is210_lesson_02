#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Task 15
from decimal import Decimal
from fractions import Fraction

FLOATVAR = 0.1
DECIMALVAR = Decimal("0.1")
FRACTIONVAR = Fraction(1, 10)

#Task 16
DF_EQUALITY = DECIMALVAR == FRACTIONVAR
print DF_EQUALITY

ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
print ARE_INEQUAL