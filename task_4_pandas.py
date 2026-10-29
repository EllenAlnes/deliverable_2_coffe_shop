
import numpy as np
import pandas as pd
from task_3_cleaning import compute_refund_ratio


# make a dummy version of the function from task 1 (last deloppgave)
def list_of_dict_opg1():
    a = [
        {"timestamp": "2026-10-15 08:01:22", "register_id": "POS_01", "item": "Espresso", "price": 3.11, "currency": "NOK", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 08:01:39", "register_id": "POS_01", "item": "Sandwich", "price": 7.43, "currency": "EUR", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 14:02:14", "register_id": "POS_01", "item": "Latte", "price": 4.72, "currency": "NOK", "status": "CANCELLED"},
        {"timestamp": "2026-10-15 14:04:42", "register_id": "POS_01", "item": "Sandwich", "price": 7.43, "currency": "NOK", "status": "REFUND"},
        {"timestamp": "2026-10-15 09:30:42", "register_id": "POS_01", "item": "Cappuccino", "price": 3.75, "currency": "NOK", "status": "REFUND"}
    ]
    return a



def chrono(df: pd.DataFrame) -> pd.DataFrame:
    """Creates DataFrame of a list of dictionaries. Sorts the transactions by timestamps.

    Arguments:
        df: DataFrame containing information of transactions.

    Returns:
        DataFrame with transactions in chronological order.
    """
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp").sort_values("timestamp")
    return df

test = chrono(pd.DataFrame(list_of_dict_opg1())) 


def one_hour(a_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Calculates total price for each product within 1-hour windows.

    Arguments:
        a_dataframe: dataframe sorted by timestamp, containing transactions.

    Returns:
        DataFrame sorted by 1-hour windows. One row for each item, within each 1-hour window.
    """   
    return a_dataframe.groupby("item").resample("1h")["price"].sum() 

#print(one_hour(test))


def by_status(b_dataframe: pd.DataFrame) -> pd.pivot_table:
    """Creates pivot table, sorting item revenue across status "SUCCESS", "REFUND" and "CANCELLED".

    Arguments:
        b_dataframe: dataframe sorted by timestamp, containing transactions.

    Returns:
        Pivot table.
    """    
    return pd.pivot_table(
        b_dataframe,
        index="item",
        columns="status",
        values="price",
        aggfunc="sum",
        fill_value=0
    )
#print(by_status(test))


def use_ratio(c_dataframe: pd.DataFrame) -> np.array:
    """Calculates the ratio between element-wise sales and refund values in given DataFrame.
        
        Arguments:
            c_dataframe: A dataframe containing transactions, either a sale, refund or cancelled transaction.

        Returns:
            Array containing the sales/refund ratio element-wise.
        """
    counts = c_dataframe.groupby(["item", "status"]).size().unstack(fill_value=0)
    success_arr = counts["SUCCESS"].to_numpy()
    refund_arr = counts["REFUND"].to_numpy()

    return compute_refund_ratio(refund_arr, success_arr)
 

print(use_ratio(test))