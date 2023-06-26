from hypothesis import given
from hypothesis import strategies as st

from roman_numeral_converter.stack_conversions import convert_stack_to_number_list, convert_number_list_to_stack


@given(roman_numeral=st.text(alphabet="ivxlcdm"))
def test_convert_lowercase_stack_to_number_list_and_back(roman_numeral):
    number_list = convert_stack_to_number_list(roman_numeral)
    assert convert_number_list_to_stack(number_list) == roman_numeral

@given(roman_numeral=st.text(alphabet="IVXLCDM"))
def test_convert_uppercase_stack_to_number_list_and_back(roman_numeral):
    number_list = convert_stack_to_number_list(roman_numeral)
    assert convert_number_list_to_stack(number_list, lowercase=False) == roman_numeral