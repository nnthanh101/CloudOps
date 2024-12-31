import logging
from runbooks.calculator import Calculator
from runbooks.utils import validate_input
from runbooks.config import DEFAULT_CONFIG
from runbooks.exceptions import InvalidOperationError, InputValidationError

# Configure logging
logging.basicConfig(filename=DEFAULT_CONFIG["log_file"], level=logging.DEBUG if DEFAULT_CONFIG["debug"] else logging.INFO)


def main():
    """CLI interface for Calculator with improved error handling."""
    try:
        calc = Calculator(precision=DEFAULT_CONFIG['precision'])
        operations = {
            '+': calc.add,
            '-': calc.subtract,
            '*': calc.multiply,
            '/': calc.divide
        }

        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation not in operations:
            raise InvalidOperationError(f"Invalid operation '{operation}'. Choose from +, -, *, /.")

        x = validate_input(input("Enter first number: "))
        y = validate_input(input("Enter second number: "))

        result = operations[operation](x, y)
        print(f"Result: {result}")

    except (InvalidOperationError, InputValidationError) as e:
        logging.error(e)
        print(f"Error: {e}")
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print(f"Critical Error: {e}")


if __name__ == "__main__":
    main()
