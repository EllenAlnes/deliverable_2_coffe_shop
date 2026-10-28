
import pandas as pd
from task_3_cleaning import clean_outliers, compute_refund_ratio
from task_4_pandas import chrono, one_hour, by_status, use_ratio

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

# task 5-4: Apply NumPy outlier cleaning to remove 999 price glitches.
dummy_df["price"] = clean_outliers(dummy_df)

# task 5-5: Apply currency correction: multiply price by 10 for all transactions where currency == "NOK" .

dummy_df.loc[dummy_df["currency"] == "NOK", ["price"]] *= 10
dummy_df.to_csv("cleaned_transactions.csv")

# task 5-6: Generate resampled reports, pivot tables and refund ratios.

chronologically = chrono(dummy_df)
hourly_revenue = one_hour(chronologically)
hourly_revenue.to_json("hourly_revenue.json") # A JSON report containing total revenue per hour per item.

revenue_pivot = by_status(dummy_df)
revenue_pivot.to_csv("status_pivot_table.csv") # A CSV file containing a pivot table of total transaction revenue grouped by item across status categories.

rat_items = pd.DataFrame(use_ratio(dummy_df))
rat_items.to_csv("rat_items.csv", index=False) # A CSV table containing refund ratios for each itemtype.



