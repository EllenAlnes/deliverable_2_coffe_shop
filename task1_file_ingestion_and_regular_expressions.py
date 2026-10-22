from pathlib import Path

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
        file
        encoding
        
    Returns
        tuple: tuple with the file data and the encoding used."""
    
    try:
        # Try to read the file with UTF-8 encoding
        with open(input_file, encoding="utf-8") as file:
            file_data = file.read()
            encoding_used = "utf-8"

    except UnicodeDecodeError:
        # If UTF-8 fails, try ISO-8859-1/Latin-1 encoding
        with open(input_file, encoding="iso-8859-1") as file:
            file_data = file.read()
            encoding_used = "ISO-8859-1"

    return file_data, encoding_used


# Testing the function on one of the files
test_file = Path("data/2026/library_cafe/POS_02/register_sales.log")

file_data, encoding_used = read_file(test_file)

print(f"Encoding used: {encoding_used}")
print(file_data[:500])  # prints the first 500 signs
