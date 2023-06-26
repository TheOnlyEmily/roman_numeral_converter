from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number
from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral

def convert_stack_to_number_list(roman_numeral_stack: str) -> list[int]:
    """
    Converts a string of atomic roman numerals into a list of integers.

    :param roman_numeral_stack: The string of atomic roman numerals to convert.
    :return: The list of integers.

    """
    return list(convert_atomic_roman_numeral_to_number(atomic_rn) for atomic_rn in roman_numeral_stack)

def convert_number_list_to_stack(number_list: list[int], lowercase: bool=True) -> str:
    """
    Converts a list of integers into a string of atomic roman numerals.

    :param number_list: The list of integers to convert.
    :param lowercase: Whether or not to convert to lowercase.
    :return: The string of atomic roman numerals.

    """
    return ''.join(convert_number_to_atomic_roman_numeral(n, lowercase=lowercase) for n in number_list)