from pathlib import Path
import json

from task1_file_ingestion_and_regular_expressions import read_file
from task1_file_ingestion_and_regular_expressions import parse_log
from task2_recursive_utility_functions import find_log_files
from task2_recursive_utility_functions import find_active_registers

# find_log_files(directory)	    Finner .log-filer i mapper og undermapper og returnerer en liste med Path-objekter.
# find_active_registers(data)   Går rekursivt gjennom nøstede dictionaries og lister og returnerer et set med aktive register-ID-er.
# read_file(input_file)	        Leser én fil og returnerer filinnholdet og tegnkodingen.
# parse_log(file_text_content)	Leser logginnhold linje for linje og returnerer gyldige transaksjoner som dictionaries.

#til oppgave 2 i task5
# listoflogs = (bruke funksjonen task 2)
# co_en = [] # list of tuples containing (file_text_content, encoding_used)  
# co_en = [read_file(log) for log in listoflogs] 

# ------ task 5.1 ------

# Task 1 find all log files recursively
data_dictionary = Path("data/2026")
log_files = find_log_files(data_dictionary)

print(f"Number of log files found: {len(log_files)}")

for log_file in sorted(log_files):
    print(log_file)

# Store confuguration - data from store-config.json
config_path = Path("data/store_config.json")

config_text, encoding_used = read_file(config_path)
# json.loads konverts text into python datastructure with dictionaries and lists
# loads - string of text, while load takes a fileobject
config_data = json.loads(config_text)

# Find all active register IDs
active_registers = find_active_registers(config_data)

# Print register information by store in config file
for region in config_data["regions"]:
    for store in region["stores"]:
        print(store["name"])

        for register in store["registers"]:
            if register["active"]:
                status = "Active"
            else:
                status = "Inactive"

            print(f"{register["id"]}, {status}")

# print
print(f"Number of log files found: {len(log_files)}")
# sorted sorts the set alfabeticly
print(f"Active register IDs form config: {sorted(active_registers)}")

# ------ task 5.2 ------
# Info:
# Dere har allerede disse variablene i task_5.py:
# log_files - en liste med Path-objekter for alle ni loggfilene.
# active_registers - et sett med aktive register-ID-er fra konfigurasjonen.
# Og dere har funksjonene:
# read_file(log_file) - leser innholdet fra én fil og håndterer tegnkodingen.
# parse_log(file_text_content) - parser tekstinnholdet og returnerer gyldige transaksjoner som dictionaries.
# Mål: behandle hver loggfil, en om gangen og samle alle transaksjonene i en felles liste

# Create empty list for all transactions
all_transactions = []

# går gjennom alle filene en etter en
for file in log_files:
    file_text_content, encoding_used = read_file(log_file)

    # parsing through the content
    transactions = parse_log(file_text_content)

    # collecting all transactions into one list
    # using extend since transactions alredy is a list, and we want to combind the lists
    all_transactions.extend(transactions)

print(f"Number of transactions (combined): {len(all_transactions)}")
