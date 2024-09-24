import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter, numbers = extract_delimiter_and_numbers(numbers)
    split_numbers = split_numbers_by_delimiter(numbers, delimiter)
    return calculate_sum(split_numbers)

def extract_delimiter_and_numbers(numbers: str) -> tuple:
    """Extracts the delimiter and the numbers from the input string."""
    default_delimiters = ',|\n'
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers.split("\n", 1)
        custom_delimiter = re.escape(delimiter_part[2:].strip('[]'))
        return custom_delimiter, numbers
    return default_delimiters, numbers

def split_numbers_by_delimiter(numbers: str, delimiter: str) -> list:
    """Splits the numbers using the given delimiter."""
    return re.split(delimiter, numbers)

def calculate_sum(split_numbers: list) -> int:
    """Calculates the sum of valid numbers and checks for negative numbers."""
    total = 0
    negatives = []
    
    for num in split_numbers:
        if num:
            value = int(num)
            total += handle_value(value, negatives)
    
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return total

def handle_value(value: int, negatives: list) -> int:
    """Handles a single value, checking for negatives and values over 1000."""
    if value < 0:
        negatives.append(value)
        return 0
    elif value <= 1000:
        return value
    return 0

