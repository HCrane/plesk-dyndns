# -*- coding: utf-8 -*-

import pytest
from plesk_dyndns.skeleton import fib

__author__ = "Emanuel Moser"
__copyright__ = "Emanuel Moser"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
