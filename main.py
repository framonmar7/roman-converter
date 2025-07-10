from cli.runner import run_cli
from errors.exceptions import (
    RomanConverterError,
    InvalidRangeError,
    InvalidRomanSyntaxError,
)

def main() -> None:
    try:
        run_cli()
    except (InvalidRangeError, InvalidRomanSyntaxError) as e:
        print(f"🚨 {type(e).__name__}: {e}")
    except RomanConverterError as e:
        print(f"⚠️ RomanConverterError: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}: {e}")
        raise

if __name__ == "__main__":
    main()
