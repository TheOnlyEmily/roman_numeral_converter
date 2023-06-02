from hypothesis import strategies as st
from hypothesis import given
from roman_numeral_converter.stack_conversions import convert_stack_to_number_list

@given(roman_numeral=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_a_list_of_equal_length_to_input_roman_numeral_string(roman_numeral):
    assert len(roman_numeral) == len(convert_stack_to_number_list(roman_numeral))

@given(roman_numeral=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_a_list_of_all_integers(roman_numeral):
    assert all(type(i) is int for i in convert_stack_to_number_list(roman_numeral))