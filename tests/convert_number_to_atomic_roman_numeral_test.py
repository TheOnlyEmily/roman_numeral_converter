import pytest
from hypothesis import given
import hypothesis.strategies as st
from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral, InvalidNumberForAtomicRomanNumeralConversionError


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

@given(invalid_number=st.integers(max_value=0))
def test_raises_InvalidNumberForAtomicRomanNumeralConversionError_given_negative_number(invalid_number):
    with pytest.raises(InvalidNumberForAtomicRomanNumeralConversionError):
        convert_number_to_atomic_roman_numeral(invalid_number)