from hypothesis import given
import hypothesis.strategies as st
from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number, convert_number_to_atomic_roman_numeral

@given(valid_number=st.sampled_from([1, 5, 10, 50, 100, 500, 1000]), return_lowercase=st.booleans())
def test_that_numbers_converted_into_atomic_roman_numerals_convert_back_into_the_same_number(valid_number, return_lowercase):
    atomic_roman_numeral = convert_number_to_atomic_roman_numeral(valid_number, return_lowercase)
    resulting_number = convert_atomic_roman_numeral_to_number(atomic_roman_numeral)
    assert valid_number == resulting_number