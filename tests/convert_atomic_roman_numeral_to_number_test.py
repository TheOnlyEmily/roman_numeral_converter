import pytest
import hypothesis.strategies as st
from hypothesis import given
from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number, InvalidAtomicRomanNumeralError

# TODO add functionality for dealing with capitalized atomic roman numerals (ex. I, V, X, etc.)
# TODO add exception for inputs that are more than one character long

def test_that_i_converts_to_1():
    assert convert_atomic_roman_numeral_to_number('i') == 1

def test_that_v_converts_to_5():
    assert convert_atomic_roman_numeral_to_number('v') == 5

def test_that_x_converts_to_10():
    assert convert_atomic_roman_numeral_to_number('x') == 10

def test_that_l_converts_to_50():
    assert convert_atomic_roman_numeral_to_number('l') == 50

def test_that_c_converts_to_100():
    assert convert_atomic_roman_numeral_to_number('c') == 100

def test_that_d_converts_to_500():
    assert convert_atomic_roman_numeral_to_number('d') == 500

def test_that_m_converts_to_1000():
    assert convert_atomic_roman_numeral_to_number('m') == 1000

@given(invalid_chr=st.characters(blacklist_characters=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_that_characters_that_are_not_valid_automic_roman_numerals_raises_an_expection(invalid_chr):
    with pytest.raises(InvalidAtomicRomanNumeralError):
        convert_atomic_roman_numeral_to_number(invalid_chr)

@given(invalid_chr=st.characters(blacklist_characters=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_that_InvalidAtomicRomanNumeralError_keeps_offending_character_as_invalid_numeral_property(invalid_chr):
    try:
        convert_atomic_roman_numeral_to_number(invalid_chr)
    except InvalidAtomicRomanNumeralError as e:
        assert e.invalid_numeral == invalid_chr