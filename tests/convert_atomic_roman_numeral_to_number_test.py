from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number

# TODO add exception for characters that aren't valid roman numerals 
# TODO add functionality for dealing with capitalized atomic roman numerals (ex. I, V, X, etc.)
# TODO add exception for inputs that are more than one character long
# TODO complete basic atomic numeral conversion functionality

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