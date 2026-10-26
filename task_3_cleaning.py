
import numpy as np
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


# make cleaning function:
def clean_outliers(df: pd.DataFrame) -> np.array:  
    """Changes outlying transactions values dataframe, to the meadian of valid transactions.
    
        Arguments:
            df: DataFrame with invalid outlying price values.
    
        Returns:
            Array containing outlier-cleaned transactions.
        """
    # converts price values to array
    cleaned = df["price"].to_numpy()

    mu = np.mean(cleaned)
    sigma = np.std(cleaned)

    # gather outlying values.
    outliers = cleaned > mu + 3*sigma

    valid_prices = cleaned[~outliers]
    median_valid = np.median(valid_prices)

    # replaces all outlier values in cleaned, with the median of the valid prices.
    cleaned[outliers] = median_valid

    return cleaned

#test = clean_outliers("data/2026/library_cafe/POS_01/register_sales.log")


def compute_refund_ratio(sales_count: np.ndarray, refund_count: np.ndarray) -> np.ndarray:
    """Calculates the ratio between element-wise sales and refund values.
    
        Arguments:
            sales_count: Array of the sales count for each element.
            
            refund_count: Array of the refund count for each element.

        Returns:
            Array containing the sales/refund ratio element-wise.
        """
    ratios = []
    for ref, sale in zip(refund_count, sales_count):
        rat = ref / (sale + 1e-6)
        ratios.append(rat)
    ratios_arr = np.array(ratios)

    return ratios_arr

    
