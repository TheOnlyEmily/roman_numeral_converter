from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number

def test_that_i_converts_to_1():
    assert convert_atomic_roman_numeral_to_number('i') == 1

def test_that_v_converts_to_5():
    assert convert_atomic_roman_numeral_to_number('v') == 5

def test_that_x_converts_to_10():
    assert convert_atomic_roman_numeral_to_number('x') == 10