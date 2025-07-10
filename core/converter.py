from core.constants import ROMAN_NUMERALS, ROMAN_VALUES
from errors.exceptions import InvalidRangeError, InvalidRomanSyntaxError

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

def roman_to_decimal(roman_number: str) -> int:
    roman_number = roman_number.upper()
    index = 0
    total = 0

    while index < len(roman_number):
        current = roman_number[index]
        next_char = roman_number[index + 1] if index + 1 < len(roman_number) else ""

        if current not in ROMAN_VALUES:
            raise InvalidRomanSyntaxError(f"Invalid character: '{current}'")

        current_value = ROMAN_VALUES[current]
        next_value = ROMAN_VALUES.get(next_char, 0)

        if next_value > current_value:
            total += next_value - current_value
            index += 2
        else:
            total += current_value
            index += 1

    if decimal_to_roman(total) != roman_number:
        raise InvalidRomanSyntaxError(f"Malformed Roman numeral: '{roman_number}'")

    return total
