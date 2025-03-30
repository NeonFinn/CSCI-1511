import pytest
from Lab11_fbaldwin3 import rotation_adjustment

def test_in_range():
    expected = 100
    actual = rotation_adjustment(100)
    assert actual == expected

def test_over():
    expected = 100
    actual = rotation_adjustment(460)
    assert actual == expected

def test_negative():
    expected = 260
    actual = rotation_adjustment(-100)
    assert actual == expected
