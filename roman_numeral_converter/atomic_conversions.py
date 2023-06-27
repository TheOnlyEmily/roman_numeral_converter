# TODO Add documentation regarding convert_atomic_roman_numeral_to_number's arguments and return value

def convert_atomic_roman_numeral_to_number(roman_numeral: str) -> int:
    """
    Converts a given atomic roman numeral to an integer.
    
    :raises: InvalidAtomicRomanNumeralError when given a string that is not 
    a lower or uppercase version of an atomic roman numeral (ex. i, v, x, etc.)
    """
    match roman_numeral.lower():
        case 'i':
            return 1
        case 'v':
            return 5
        case 'x':
            return 10
        case 'l':
            return 50
        case 'c': 
            return 100
        case 'd':
            return 500
        case 'm':
            return 1000

# TODO Add documentation regarding convert_number_to_atomic_roman_numeral's arguments and return value

def convert_number_to_atomic_roman_numeral(n: int, lowercase: bool=True) -> str:
    """Turns an integer into its atomic roman numeral representation."""
    match n:
        case 1:
            return_value = 'i'
        case 5:  
            return_value = 'v'
        case 10:
            return_value = 'x'
        case 50:
            return_value = 'l'
        case 100:
            return_value = 'c'
        case 500:
            return_value = 'd'
        case 1000:
            return_value = 'm'
    return return_value if lowercase else return_value.upper()

def is_valid_atomic_roman_numeral(atomic_roman_numeral: str) -> bool:
    """Returns True if the given atomic roman numeral is valid."""
    return atomic_roman_numeral.lower() in ['i', 'v', 'x', 'l', 'c', 'd', 'm']

def can_convert_to_atomic_roman_numeral(n: int) -> bool:
    """Returns True if the given number can be converted to an atomic roman numeral."""
    return n in [1, 5, 10, 50, 100, 500, 1000]