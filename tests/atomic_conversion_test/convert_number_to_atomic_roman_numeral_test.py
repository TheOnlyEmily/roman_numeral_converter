import pytest
from hypothesis import given
import hypothesis.strategies as st
from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral


def test_1_converts_to_i():
    assert convert_number_to_atomic_roman_numeral(1) == 'i'

def test_5_converts_to_v():
    assert convert_number_to_atomic_roman_numeral(5) == 'v'

def test_10_converts_to_x():
    assert convert_number_to_atomic_roman_numeral(10) == 'x'

def test_50_converts_to_l():
    assert convert_number_to_atomic_roman_numeral(50) == 'l'

def test_100_converts_to_c():
    assert convert_number_to_atomic_roman_numeral(100) == 'c'

def test_500_converts_to_d():
    assert convert_number_to_atomic_roman_numeral(500) == 'd'

def test_1000_converts_to_m():
    assert convert_number_to_atomic_roman_numeral(1000) == 'm'

@given(valid_number=st.sampled_from([1, 5, 10, 50, 100, 500, 1000]))
def test_returns_uppercase_atomic_roman_numeral_when_the_lowercase_argument_is_false(valid_number):
    lowercase = False
    assert convert_number_to_atomic_roman_numeral(valid_number, lowercase).isupper()

@given(valid_number=st.sampled_from([1, 5, 10, 50, 100, 500, 1000]))
def test_return_lowercase_atomic_roman_numeral_when_lowercase_argument_is_true(valid_number):
    lowercase = True
    assert convert_number_to_atomic_roman_numeral(valid_number, lowercase).islower()