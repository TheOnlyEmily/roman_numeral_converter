from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral


def test_1_converts_to_i():
    assert convert_number_to_atomic_roman_numeral(1) == 'i'