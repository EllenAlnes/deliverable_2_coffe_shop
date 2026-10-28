import re
from pathlib import Path
import pandas as pd
from task_3_cleaning import clean_outliers

dummy_df = pd.DataFrame([
    {
        "timestamp": "2026-10-15 08:11:35",
        "register_id": "POS_01",
        "item": "Muffin",
        "price": 999.00,
        "currency": "EUR",
        "status": "SUCCESS"
    },
    {
        "timestamp": "2026-10-15 08:14:34",
        "register_id": "POS_01",
        "item": "Sandwich",
        "price": 7.37,
        "currency": "USD",
        "status": "SUCCESS"
    },
    {
        "timestamp": "2026-10-15 08:16:18",
        "register_id": "POS_01",
        "item": "Espresso",
        "price": 2.76,
        "currency": "NOK",
        "status": "SUCCESS"
    },
    {
        "timestamp": "2026-10-15 08:18:52",
        "register_id": "POS_01",
        "item": "Sandwich",
        "price": 7.34,
        "currency": "EUR",
        "status": "REFUND"
    }
])

dummy_df["timestamp"] = pd.to_datetime(dummy_df["timestamp"])
#dummy_df = dummy_df.set_index("timestamp") #tror ikke denne må med her

# task 5-4: Apply NumPy outlier cleaning to remove 999 price glitches.
dummy_df["price"] = clean_outliers(dummy_df)

# task 5-5: Apply currency correction: multiply price by 10 for all transactions where
# currency == "NOK" .

dummy_df.loc[dummy_df["currency"] == "NOK", ["price"]] *= 10
#print(dummy_df)

# task 5-6: Generate resampled reports, pivot tables and refund ratios.








# OUTPUTS
# convert to csv
#dummy_df.to_csv("cleaned_transactions.csv")