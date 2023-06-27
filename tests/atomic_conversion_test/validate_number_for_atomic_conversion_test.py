from hypothesis import given, strategies as st
from roman_numeral_converter.atomic_conversions import can_convert_to_atomic_roman_numeral

def test_is_callable():
    assert callable(can_convert_to_atomic_roman_numeral)

@given(number=st.integers())
def test_takes_single_number_as_argument(number):
    can_convert_to_atomic_roman_numeral(number)

@given(number=st.integers())
def test_returns_boolean(number):
    assert isinstance(can_convert_to_atomic_roman_numeral(number), bool)

@given(invalid_number=st.integers(max_value=-1))
def test_returns_false_given_negative_numbers(invalid_number):
    assert not can_convert_to_atomic_roman_numeral(invalid_number)

@given(invalid_number=st.one_of(
    st.integers(2, 4), 
    st.integers(6, 9), 
    st.integers(11, 49),
    st.integers(51, 99),
    st.integers(101, 499),
    st.integers(501, 999)))
def test_returns_false_given_numbers_that_cannot_be_converted_to_atomic_roman_numerals(invalid_number):
    assert not can_convert_to_atomic_roman_numeral(invalid_number)

def test_returns_false_given_0():
    assert not can_convert_to_atomic_roman_numeral(0)

@given(invalid_number=st.integers(min_value=1001))
def test_returns_false_given_numbers_greater_than_1000(invalid_number):
    assert not can_convert_to_atomic_roman_numeral(invalid_number)
