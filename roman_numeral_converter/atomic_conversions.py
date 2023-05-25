def convert_atomic_roman_numeral_to_number(roman_numeral: str) -> int:
    match roman_numeral:
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