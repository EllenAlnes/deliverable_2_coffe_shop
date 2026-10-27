import re
from pathlib import Path


def read_file(input_file: Path) -> tuple[str, str]:
    """Read a file and return its content and the encoding used.
    
    Arguments:
        input_file: Path to the file to read.
        
    Returns:
        A tuple containing the file content as a string and the encoding used as a string."""
    
    try:
        # Try to read the file with UTF-8 encoding
        with input_file.open(encoding="utf-8") as file:
            file_text_content = file.read()
            encoding_used = "utf-8"

    except UnicodeDecodeError:
        # If UTF-8 fails, try ISO-8859-1/Latin-1 encoding
        with input_file.open(encoding="ISO-8859-1") as file:
            file_text_content = file.read()
            encoding_used = "ISO-8859-1"

    # Returns a tuple with file_text_content and encoding_used
    return file_text_content, encoding_used


def parse_log(file_text_content: str) -> list[dict[str, str | float]]:
    """Parse log file content and and return valid transactions.

    A parser function analyses text and extracts structured information from it according to a defined format.

    Arguments:
        file_text_content: The complete text content of a log file.

    Returns:
        A list of dictionaries containing valid transactions.
        Each dictionary contains the timestamt, register ID, item,
        price, currency, and status. The price is stored as a float.
        Lines that do not match the expected log format are ignored.
    """

    # Regex pattern for valid transactions
    # () - groups result together
    # ?P<...> names the group
    # r"..." raw string
    pattern = (
    r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] " 
    r"\[(?P<register_id>\w+)\] " 
    r"item=(?P<item>\S+) " 
    r"price=(?P<price>\d+\.\d+) "  
    r"(?P<currency>EUR|NOK|USD) " 
    r"\((?P<status>SUCCESS|REFUND|CANCELLED)\)" 
) 
    # empty list to collect the valid lines in the logfiles
    valid_transactions = []

    # splits up the file so we can work with it line by line
    for line in file_text_content.splitlines():

        # check whether this line matches the pattern
        match = re.fullmatch(pattern, line)

        # if the line is valid, extract this field
        if match:
            transaction = match.groupdict()

            # convert prise to float
            transaction["price"] = float(transaction["price"])

            # add the transaction to the list
            valid_transactions.append(transaction)

    return valid_transactions


# Temporary test of read_file() and parse_log()
# Testing the read_file function on one of the files
test_file = Path("data/2026/student_union/POS_01/register_sales.log")

file_text_content, encoding_used = read_file(test_file)

# call the parcer function
transactions = parse_log(file_text_content)

print(f"Encoding used: {encoding_used}")
print(f"Number of valid transactions: {len(transactions)}")