import pytest
from Lab11_fbaldwin3 import rotation_adjustment

def test_in_range():
    expected = '100.00'
    actual = rotation_adjustment(100)
    assert actual == expected

def test_over():
    expected = '100.00'
    actual = rotation_adjustment(460)
    assert actual == expected

def test_negative():
    expected = '260.00'
    actual = rotation_adjustment(-100)
    assert actual == expected

def test_invalid_input():
    with pytest.raises(ValueError):
        rotation_adjustment("hello")