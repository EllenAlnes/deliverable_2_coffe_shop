from pathlib import Path
import re

# Hvordan løse oppgavene?

# pathlib.Path til file path
# håndtere ulik encoding: UTF-8 og ISO-8859-1/Latin-1
# return tuple med to strings: (file_text_conect, encoding_used)

# skriv en log parser funksjon - tar data som input og strukturerer det
# bruk regular expression - re modul

# return - liste med python dictionaries, hver dict er en gyldig transaksjon


# funksjon 1 - leser filer med ulik encoding
# funksjon 2 - bruker regulære uttrykk til å hente ut transaksjoner


def read_file(input_file: Path) -> tuple[str, str]:
    """Read a file and return its content and the encoding used.
    
    Arguments:
        input_file: Path to the file to be read.
        
    Returns:
        A tuple containing the file text content and the encoding used."""
    
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


# # Testing the read_file function on one of the files
# test_file = Path("data/2026/library_cafe/POS_03/register_sales.log")

# file_text_content, encoding_used = read_file(test_file)

# print(f"Encoding used: {encoding_used}")
# print(file_text_content[:500])  # prints the first 500 signs

# Write a function that uses regular expressions to go through the files
# Example log complete log line
# [2026-10-15 08:30:00] [POS_01] item=Latte price=4.50 EUR (SUCCESS)


# Creating pattern for grouped for de data
# () - groups result together
# ?P<...> names the group
# r"..." raw string

# pattern = (
#     r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] " 
#     r"\[(?P<register_id>\w+)\] " 
#     r"item=(?P<item>\S+) " 
#     r"price=(?P<price>\d+\.\d+) "  
#     r"(?P<currency>EUR|NOK|USD) " 
#     r"\((?P<status>SUCCESS|REFUND|CANCELLED)\)" 
# ) 

# Testing if the regex pattern works
# test_line = (
#     "[2026-10-15 08:30:00] [POS_01] item=Latte price=4.50 EUR (SUCCESS)")

# match = re.fullmatch(pattern, test_line)

# if match:
#     print(match.groupdict())


def parse_log(file_text_content: str) -> list[dict]:
    # Parserfunksjonen tar imot en loggfil, undersøker den en linje om gangen go ignorerer det som ikke er gyldig linje
    """takes the result for the prior funciton as inputfile.
    Parser function that takes a input log file and analyses it line by line. 
    Keeping valid transactions and filters out any noice.
    
    Return:
        Returns a list of dictionarys whith valid transactions"""

    # Regex pattern for valid transactions
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

        #check whether this line matches the pattern
        match = re.fullmatch(pattern, line)

        # if the line is valid, extract this field
        if match:
            transaction = match.groupdict()

            # convert prise to float
            transaction["price"] = float(transaction["price"])

            # add the transaction to the list
            valid_transactions.append(transaction)

    return valid_transactions

#testing with valid and invalid lines
# test_text = (
#     "[2026-10-15 08:30:00] [POS_01] "
#     "item=Latte price=4.50 EUR (SUCCESS)\n"
#     "--- PRINTER PAPER LOW WARNING ---\n"
#     "[2026-10-15 08:31:00] [POS_01] "
#     "item=Muffin price=3.94 EUR (SUCCESS)\n"
#     "=== NETWORK SYNC OK ==="
# )

# result = parse_log(test_text)
# print(result)

# # Testing noise
# noise_text = (
#     "--- PRINTER PAPER LOW WARNING ---\n"
#     "=== NETWORK SYNC OK ==="
# )

# print(parse_log(noise_text))


# Testing the read_file function on one of the files
test_file = Path("data/2026/student_union/POS_01/register_sales.log")

file_text_content, encoding_used = read_file(test_file)

# call the parcer function
transactions = parse_log(file_text_content)
print(transactions)

print(f"Number of valid transactions: {len(transactions)}")