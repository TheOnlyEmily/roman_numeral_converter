from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number
from roman_numeral_converter.atomic_conversions import convert_number_to_atomic_roman_numeral

def convert_stack_to_number_list(roman_numeral_stack: str) -> list[int]:
    return list(convert_atomic_roman_numeral_to_number(atomic_rn) for atomic_rn in roman_numeral_stack)

def convert_number_list_to_stack(number_list: list[int]) -> str:
    return ''.join(convert_number_to_atomic_roman_numeral(n) for n in number_list)