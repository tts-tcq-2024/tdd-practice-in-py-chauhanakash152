import re

def add(numbers: str) -> int:
    """Main function to add numbers from the input string."""
    if not numbers:
        return 0
    
    delimiter, numbers = extract_delimiter_and_numbers(numbers)
    validate_input_format(numbers)
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

def validate_input_format(numbers: str):
    """Checks for invalid formats like misplaced or consecutive delimiters."""
    if has_consecutive_delimiters(numbers):
        raise ValueError("Invalid format: consecutive or misplaced delimiters")

def has_consecutive_delimiters(numbers: str) -> bool:
    """Checks if the input contains consecutive delimiters."""
    return bool(re.search(r'(,|\n)(,|\n)', numbers))

def split_numbers_by_delimiter(numbers: str, delimiter: str) -> list:
    """Splits the numbers using the given delimiter."""
    return re.split(delimiter, numbers)

def calculate_sum(split_numbers: list) -> int:
    """Calculates the sum of valid numbers and checks for negative numbers."""
    negatives = find_negatives(split_numbers)
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum_valid_numbers(split_numbers)

def find_negatives(numbers: list) -> list:
    """Finds all negative numbers in the list."""
    return [int(num) for num in numbers if num and int(num) < 0]

def sum_valid_numbers(numbers: list) -> int:
    """Sums numbers less than or equal to 1000 and skips negatives."""
    return sum(int(num) for num in numbers if num and 0 <= int(num) <= 1000)
