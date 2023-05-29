from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral


def test_1_converts_to_i():
    assert convert_number_to_atomic_roman_numeral(1) == 'i'

def test_5_converts_to_v():
    assert convert_number_to_atomic_roman_numeral(5) == 'v'

def test_10_converts_to_x():
    assert convert_number_to_atomic_roman_numeral(10) == 'x'

def test_50_converts_to_l():
    assert convert_number_to_atomic_roman_numeral(50) == 'l'

def test_100_converts_to_c():
    assert convert_number_to_atomic_roman_numeral(100) == 'c'

def test_500_converts_to_d():
    assert convert_number_to_atomic_roman_numeral(500) == 'd'