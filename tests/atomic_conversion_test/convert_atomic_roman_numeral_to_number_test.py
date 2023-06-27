import hypothesis.strategies as st
from hypothesis import given
from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number

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

@st.composite
def lower_and_uppercase_atomic_roman_numerals(draw):
    lowercase_roman_numeral = draw(st.sampled_from(['i', 'v', 'x', 'l', 'c', 'd', 'm']))
    uppercase_roman_numeral = lowercase_roman_numeral.upper()
    return lowercase_roman_numeral, uppercase_roman_numeral

@given(lower_uppercase_pair=lower_and_uppercase_atomic_roman_numerals())
def test_lower_and_uppercase_atomic_roman_numerals_become_same_number(lower_uppercase_pair):
    lowercase_roman_numeral, uppercase_roman_numeral = lower_uppercase_pair
    assert convert_atomic_roman_numeral_to_number(lowercase_roman_numeral) == convert_atomic_roman_numeral_to_number(uppercase_roman_numeral)