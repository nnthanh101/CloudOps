def validate_input(value: str) -> float:
    """Validates and converts input to float."""
    if value.strip() == "":
        raise ValueError("Input cannot be empty.")  # Directly raise for empty inputs
    
    try:
        return float(value)  # Attempt numeric conversion
    except ValueError as e:
        raise ValueError(f"Invalid input '{value}'. Must be a number.") from e
