class RomanConverterError(Exception):
    """Base class for all Roman converter exceptions."""

class InvalidRangeError(RomanConverterError):
    """Raised when a decimal number is outside the valid range (1–3999)."""
