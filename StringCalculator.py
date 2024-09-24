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
    if numbers.startswith("//"):
        return extract_custom_delimiter(numbers)
    return ',|\n', numbers


def extract_custom_delimiter(numbers: str) -> tuple:
    """Extracts the custom delimiter and numbers."""
    delimiter_part, numbers = numbers.split("\n", 1)
    custom_delimiter = re.escape(delimiter_part[2:].strip('[]'))
    return custom_delimiter, numbers


def validate_input_format(numbers: str):
    """Checks for invalid formats like misplaced or consecutive delimiters."""
    if has_consecutive_delimiters(numbers):
        raise ValueError("Invalid format: consecutive or misplaced delimiters")


def has_consecutive_delimiters(numbers: str) -> bool:
    """Checks if the input contains consecutive delimiters."""
    return re.search(r'(,|\n)(,|\n)', numbers) is not None


def split_numbers_by_delimiter(numbers: str, delimiter: str) -> list:
    """Splits the numbers using the given delimiter."""
    return re.split(delimiter, numbers)


def calculate_sum(split_numbers: list) -> int:
    """Calculates the sum of valid numbers and checks for negative numbers."""
    negatives = find_negatives(split_numbers)
    if negatives:
        raise ValueError(negative_numbers_error_message(negatives))
    return sum_valid_numbers(split_numbers)


def find_negatives(numbers: list) -> list:
    """Finds all negative numbers in the list."""
    return [to_int(num) for num in numbers if is_negative(num)]


def sum_valid_numbers(numbers: list) -> int:
    """Sums numbers less than or equal to 1000 and skips negatives."""
    return sum(to_int(num) for num in numbers if is_valid_number(num))


def is_negative(num: str) -> bool:
    """Checks if a number is negative."""
    return num and int(num) < 0


def is_valid_number(num: str) -> bool:
    """Checks if a number is between 0 and 1000."""
    return num and 0 <= int(num) <= 1000


def to_int(num: str) -> int:
    """Converts string to integer, assumes num is valid."""
    return int(num)


def negative_numbers_error_message(negatives: list) -> str:
    """Creates the error message for negative numbers."""
    return f"negatives not allowed: {', '.join(map(str, negatives))}"
