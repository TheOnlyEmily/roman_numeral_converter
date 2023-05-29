# TODO Add logic to InvalidAtomicNumeralError so it can give more specific messages

class InvalidAtomicRomanNumeralError(ValueError):
    """An exception raised when convert_atomic_roman_numeral_to_number is given
    an invalid atomic roman numeral."""

    def __init__(self, invalid_numeral: str, message: str="invalid atomic roman numeral") -> None:
        super().__init__(message)
        self.invalid_numeral = invalid_numeral


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
        case _:
            raise InvalidAtomicRomanNumeralError(roman_numeral)

# TODO work on convert_number_to_atomic_roman_numeral until 

def convert_number_to_atomic_roman_numeral(n: int) -> str:
    """Turns an integer into its atomic roman numeral representation."""
    match n:
        case 1:
            return 'i'
        case 5: 
            return 'v'
        case 10:
            return 'x'
        case 50:
            return 'l'