from roman_numeral_converter.atomic_conversions import convert_atomic_roman_numeral_to_number

def convert_stack_to_number_list(roman_numeral_stack: str) -> list[int]:
    return list(convert_atomic_roman_numeral_to_number(atomic_rn) for atomic_rn in roman_numeral_stack)

def convert_number_list_to_stack(number_list: list[int]) -> str:
    return ''.join('i' for _ in number_list)