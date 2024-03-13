import pytest
from backend.routes import payloader

def test_1():
    assert True

def test_payloader():
    assert payloader(1, 2) == 3
