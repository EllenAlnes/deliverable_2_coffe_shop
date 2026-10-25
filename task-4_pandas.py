
import numpy as numpy
import pandas as pd


# make a dummy version of the function from task 1 (last deloppgave)
def list_of_dict_opg1():
    a = [
        {"timestamp": "2026-10-15 08:01:22", "register_id": "POS_01", "item": "Espresso", "price": 3.11, "currency": "NOK", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 08:01:39", "register_id": "POS_01", "item": "Sandwich", "price": 7.43, "currency": "EUR", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 08:02:14", "register_id": "POS_01", "item": "Latte", "price": 4.72, "currency": "NOK", "status": "CANCELLED"},
        {"timestamp": "2026-10-15 08:04:42", "register_id": "POS_01", "item": "Cappuccino", "price": 3.75, "currency": "NOK", "status": "REFUND"}
    ]
    return a

def chrono(transactions: list[dict]) -> pd.DataFrame:
    """Creates DataFrame of a list of dictionaries. Sorts the transactions by timestamps.

    Arguments:
        transactions: List of dictionaries containing information of transactions.

    Returns:
        DataFrame with transactions in chronological order.
    """
    df = pd.DataFrame(transactions)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp").sort_values("timestamp")
    return df

test = chrono(list_of_dict_opg1())
#print(test.groupby("item"))

def one_hour(a_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Calculates total price for each product within 1-hour windows.

    Arguments:
        a_dataframe: dataframe sorted by timestamp, containing transactions.

    Returns:
        DataFrame sorted by 1-hour windows. One row for each item, within each 1-hour window.
    """    
    a_dataframe = a_dataframe.groupby(["item"]).resample("1h").sum()  
    #a_dataframe = a_dataframe.resample("1h")


    return a_dataframe

print(one_hour(test))

#.reset_index()
