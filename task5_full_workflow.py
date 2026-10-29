import re
from pathlib import Path
import pandas as pd
from task_3_cleaning import clean_outliers
from task_4_pandas import chrono, one_hour, by_status, use_ratio
import json
from pathlib import Path

import pandas as pd

from task1_file_ingestion_and_regular_expressions import parse_log, read_file
from task2_recursive_utility_functions import find_active_registers, find_log_files

# find_log_files(directory)	    Finner .log-filer i mapper og undermapper og returnerer en liste med Path-objekter.
# find_active_registers(data)   Går rekursivt gjennom nøstede dictionaries og lister og returnerer et set med aktive register-ID-er.
# read_file(input_file)	        Leser én fil og returnerer filinnholdet og tegnkodingen.
# parse_log(file_text_content)	Leser logginnhold linje for linje og returnerer gyldige transaksjoner som dictionaries.

# ------ task 5.1 ------

# Task 1 find all log files recursively
data_dictionary = Path("data/2026")
log_files = find_log_files(data_dictionary)

print(f"Number of log files found: {len(log_files)}")

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

# Task 5.2: Process each log file one at a time and collect all transactions into a single list.
# Create empty list for all transactions
all_transactions = []

# Read and parse each log file
# Collect all transactions into one combined list
for log_file in sorted(log_files):
    file_text_content, encoding_used = read_file(log_file)
    transactions = parse_log(file_text_content)
    all_transactions.extend(transactions)

print(f"Number of transactions: {len(all_transactions)}")

# ------ task 5.3 ------
# Task 5.3 Build the initial DataFrame
df = pd.DataFrame(all_transactions)

# Convert timestamt to datetime
#df["timestamp"] = pd.to_datetime(df["timestamp"])

# Set timestamp as index
#df = df.set_index("timestamp")

# Sort transactions chronologically
#df = df.sort_index()

# Check the DataFrame
print(df.head(20))
df.info()    # Gives info about the DataFrame
print(f"Number of transactions: {len(df)}")
print(df["register_id"].value_counts())



# task 5-4: Apply NumPy outlier cleaning to remove 999 price glitches.
df["price"] = clean_outliers(df)

# task 5-5: Apply currency correction: multiply price by 10 for all transactions where currency == "NOK" .

df.loc[df["currency"] == "NOK", ["price"]] *= 10
df.to_csv("cleaned_transactions.csv")

# task 5-6: Generate resampled reports, pivot tables and refund ratios.

chronologically = chrono(df)
hourly_revenue = one_hour(chronologically)
hourly_revenue.to_json("hourly_revenue.json") # A JSON report containing total revenue per hour per item.

revenue_pivot = by_status(df)
revenue_pivot.to_csv("status_pivot_table.csv") # A CSV file containing a pivot table of total transaction revenue grouped by item across status categories.

rat_items = pd.DataFrame(use_ratio(df))
rat_items.to_csv("rat_items.csv", index=False) # A CSV table containing refund ratios for each itemtype.



