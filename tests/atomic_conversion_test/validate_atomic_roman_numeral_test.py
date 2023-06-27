import pytest
from hypothesis import given, strategies as st

from roman_numeral_converter.atomic_conversions import is_valid_atomic_roman_numeral

def test_that_is_valid_roman_numeral_is_callable():
    assert callable(is_valid_atomic_roman_numeral)

@given(any_string=st.text())
def test_that_is_valid_roman_numeral_takes_a_single_string_argument(any_string):
    is_valid_atomic_roman_numeral(any_string)

@given(any_string=st.text())
def test_that_is_valid_roman_numeral_returns_a_boolean(any_string):
    assert isinstance(is_valid_atomic_roman_numeral(any_string), bool)

@given(valid_chr=st.text(min_size=1, max_size=1, alphabet='ivxlcdmIVXLCDM'))
def test_that_valid_atomic_roman_numerals_cause_function_to_return_true(valid_chr):
    assert is_valid_atomic_roman_numeral(valid_chr)

@given(invalid_chr=st.characters(blacklist_characters=['i', 'v', 'x', 'l', 'c', 'd', 'm', 'I', 'V', 'X', 'L', 'C', 'D', 'M']))
def test_that_characters_that_are_not_valid_automic_roman_numerals_cause_function_to_return_false(invalid_chr):
    assert not is_valid_atomic_roman_numeral(invalid_chr)

@given(invalid_string=st.text(min_size=2))
def test_strings_are_invalid_atomic_roman_numerals(invalid_string):
    assert not is_valid_atomic_roman_numeral(invalid_string)