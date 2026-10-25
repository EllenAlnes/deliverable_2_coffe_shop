
import numpy as np

# make cleaning function:
def clean_outliers(paylog: str) -> np.array:  # MÅ ENDRE SÅ DEN TAR EN VILKÅRLIG ARRAY SOM INPUT
    """Changes outlying transactions values in payment log, to the mean of valid transactions.
    
        Arguments:
            paylog: name of file of all transactions in a cash register.
    
        Returns:
            Array containing outlier-cleaned transactions.
        """
    # list of all transactions
    #pretrans = []
    
    #with open(paylog) as f:
    #    for tran in f:
    #        for word in tran.split():
    #            if word.startswith("price"):
    #                pretrans.append(float(word.split("=")[1]))

    # convert list to 1D array
    cleaned = np.array(pretrans)

    # change invalid transactions in the array (by using deviation function) with mean value of the array
    mu = np.mean(cleaned)
    sigma = np.std(cleaned)

    for i in range(len(cleaned)):
        if cleaned[i] - mu > 3*sigma:
            cleaned[i] = mu

    return cleaned

#test = clean_outliers("data/2026/library_cafe/POS_01/register_sales.log")

# make a dummy version of the function from task 1 (last deloppgave)
def list_of_dict_opg1():
    a = [
        {"timestamp": "2026-10-15 08:01:22", "register_id": "POS_01", "item": "Espresso", "price": 3.11, "currency": "NOK", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 08:01:39", "register_id": "POS_01", "item": "Sandwich", "price": 7.43, "currency": "EUR", "status": "SUCCESS"},
        {"timestamp": "2026-10-15 08:02:14", "register_id": "POS_01", "item": "Latte", "price": 4.72, "currency": "NOK", "status": "CANCELLED"},
        {"timestamp": "2026-10-15 08:04:42", "register_id": "POS_01", "item": "Cappuccino", "price": 3.75, "currency": "NOK", "status": "REFUND"}
    ]
    return a

# need a function for making arrays of sales and refunds each
#def values_from_status(transactions: list[dict], stat: str) -> np.array: 
#    prices = []
#    for i in transactions:
#        if i["status"] == stat:
#            prices.append(i["price"])
#
#    prices_arr = np.array(prices)
#    return prices_arr

#print(values_from_status(list_of_dict_opg1(), "SUCCESS"))
#print(values_from_status(list_of_dict_opg1(), "REFUND"))

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

    
