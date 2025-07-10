from core.constants import ROMAN_NUMERALS
from errors.exceptions import InvalidRangeError

def decimal_to_roman(decimal_number: int) -> str:
    if not (1 <= decimal_number <= 3999):
        raise InvalidRangeError(f"{decimal_number} is outside the range 1–3999.")

    roman_numeral = ""
    remaining = decimal_number

    for value, numeral in ROMAN_NUMERALS.items():
        while remaining >= value:
            roman_numeral += numeral
            remaining -= value

    return roman_numeral
