class RomanConverterError(Exception):
    """Base class for all Roman converter exceptions."""

class InvalidRangeError(RomanConverterError):
    """Raised when a decimal number is outside the valid range (1–3999)."""

class InvalidRomanSyntaxError(RomanConverterError):
    """Raised when a Roman numeral has incorrect syntax."""
