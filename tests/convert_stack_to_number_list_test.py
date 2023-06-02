from hypothesis import strategies as st
from hypothesis import given, assume
from roman_numeral_converter.stack_conversions import convert_stack_to_number_list

@given(roman_numeral=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_a_list_of_equal_length_to_input_roman_numeral_string(roman_numeral):
    assert len(roman_numeral) == len(convert_stack_to_number_list(roman_numeral))

@given(roman_numeral=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_a_list_of_all_integers(roman_numeral):
    assert all(type(i) is int for i in convert_stack_to_number_list(roman_numeral))

@given(roman_numeral1=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']), roman_numeral2=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_different_lists_for_different_roman_numerals(roman_numeral1, roman_numeral2):
    assume(roman_numeral1 != roman_numeral2)
    assert convert_stack_to_number_list(roman_numeral1) != convert_stack_to_number_list(roman_numeral2)

@given(roman_numeral=st.text(alphabet=['i', 'v', 'x', 'l', 'c', 'd', 'm']))
def test_returns_only_valid_numbers(roman_numeral):
    VALID_NUMBERS = [1, 5, 10, 50, 100, 500, 1000]
    assert all(n in VALID_NUMBERS for n in convert_stack_to_number_list(roman_numeral))