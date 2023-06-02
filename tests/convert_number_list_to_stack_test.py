from hypothesis import given, assume
from hypothesis import strategies as st
from roman_numeral_converter.stack_conversions import convert_number_list_to_stack

@given(number_list=st.lists(elements=st.sampled_from([1, 5, 10, 50, 100, 500, 1000])))
def test_takes_a_list_of_ints_and_returns_a_string(number_list):
    assert type(convert_number_list_to_stack(number_list)) is str

@given(number_list=st.lists(elements=st.sampled_from([1, 5, 10, 50, 100, 500, 1000])))
def test_returns_roman_numeral_stack_the_same_length_as_list(number_list):
    assert len(number_list) == len(convert_number_list_to_stack(number_list))