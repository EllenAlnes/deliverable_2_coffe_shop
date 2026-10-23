
import numpy as np

# create function that replaces outlying prices with better
# convert all prices to 1D array
# detect outliers (formula for deviation)
# replaces these with median of VALID prices
# returns cleaned 1D array
# use function for each file: one file for each cash register in each location

# make cleaning function:
def clean_outliers(paylog: str) -> np.array:
    # fetch all prices, convert to list
    preprizes = []

    with open(paylog) as f:
        for tran in f:
            for word in tran.split():
                if word.startswith("price"):
                    preprizes.append(float(word.split("=")[1]))

    # convert list to 1D array
    prize_arr = np.array(preprizes)

    # change invalid prizes in the array (by using deviation function) with mean value of the array

    mu = np.mean(prize_arr)
    sigma = np.std(prize_arr)

    for i in range(len(prize_arr)):
        if prize_arr[i] - mu > 3*sigma:
            prize_arr[i] = mu




# write out dumblist
#print(clean_outliers("data/2026/library_cafe/POS_02/register_sales.log"))




