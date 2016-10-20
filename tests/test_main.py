# -*- coding: utf-8 -*-

from decimal import Decimal

import pytest
import redpackets


class TestRedPacketsCommands(object):

    def test_split_dollar(self):
        # Total Zero
        with pytest.raises(ValueError):
            redpackets.split_dollor(0, 2)
        # Num Zero
        with pytest.raises(ValueError):
            redpackets.split_dollor(10, 0)
        # Num Float & int(Num) != Num
        with pytest.raises(ValueError):
            redpackets.split_dollor(10, 2.1)
        # Num Float & int(Num) == Num
        result = redpackets.split_dollor(10, 2.0)
        assert len(result) == 2
        assert sum(result) == Decimal('10')
        # Total < Num * Min
        with pytest.raises(ValueError):
            redpackets.split_dollor(10, 2, 6)
        result = redpackets.split_dollor(10, 2)
        assert len(result) == 2
        assert sum(result) == Decimal('10')

    def test_split_cent(self):
        # Total Zero
        with pytest.raises(ValueError):
            redpackets.split_dollor(0, 2)
        # Num Zero
        with pytest.raises(ValueError):
            redpackets.split_dollor(10, 0)
        # Total < Num * Min
        with pytest.raises(ValueError):
            redpackets.split_dollor(10, 2, 6)
        result = redpackets.split_dollor(10, 2)
        assert len(result) == 2
        assert sum(result) == Decimal('10')

    def test_cent(self):
        assert redpackets.cent(0.07) == 7

    def test_dollar(self):
        assert redpackets.dollar(7) == 0.07

    def test_mul(self):
        assert redpackets.mul(1, 0.95) == 0.95
        assert redpackets.mul(1, 0.01) == 0.01

    def test_div(self):
        assert redpackets.div(10, 2) == 5.0
        assert redpackets.div(10, 2.0) == 5.0
        assert redpackets.div(10, 2, cast_func=int) == 5
        assert redpackets.div(10, 2.0, cast_func=int) == 5
