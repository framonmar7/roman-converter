from core.constants import DECIMAL_TO_ROMAN , ROMAN_TO_DECIMAL
from errors.exceptions import InvalidRangeError, InvalidRomanSyntaxError

def decimal_to_roman(decimal_number: int) -> str:
    if not (1 <= decimal_number <= 3999):
        raise InvalidRangeError(f"{decimal_number} is outside the range 1–3999.")

    roman_number = ""
    remaining = decimal_number

    for decimal_unit, roman_symbol in DECIMAL_TO_ROMAN.items():
        while remaining >= decimal_unit:
            roman_number += roman_symbol
            remaining -= decimal_unit

    return roman_number

def roman_to_decimal(roman_number: str) -> int:
    roman_number = roman_number.upper()
    index = 0
    total = 0

    while index < len(roman_number):
        current = roman_number[index]
        next_char = roman_number[index + 1] if index + 1 < len(roman_number) else ""

        if current not in ROMAN_TO_DECIMAL:
            raise InvalidRomanSyntaxError(f"Invalid character: '{current}'")

        current_value = ROMAN_TO_DECIMAL[current]
        next_value = ROMAN_TO_DECIMAL.get(next_char, 0)

        if next_value > current_value:
            total += next_value - current_value
            index += 2
        else:
            total += current_value
            index += 1

    if decimal_to_roman(total) != roman_number:
        raise InvalidRomanSyntaxError(f"Malformed Roman number: '{roman_number}'")

    return total
