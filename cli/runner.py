from cli.parser import parse_arguments
from core.converter import decimal_to_roman, roman_to_decimal

def run_cli():
    args = parse_arguments()

    if args.decimal is not None:
        result = decimal_to_roman(args.decimal)
        print(f"{args.decimal} → {result}")

    elif args.roman is not None:
        result = roman_to_decimal(args.roman)
        print(f"{args.roman.upper()} → {result}")
