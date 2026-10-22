
import numpy as np

# create function that replaces outlying prices with better
# convert all prices to 1D array
# detect outliers (formula for deviation)
# replaces these with median of VALID prices
# returns cleaned 1D array

# use function for each file: one file for each cash register in each location

# function for finding standard deviation (or 3 standard deviations):
def deviation(listnum: np.array) -> float:
    for x in listnum:
    sum_diff = (xi - x(strek))^2
    dev = sqrt(sum_diff/(range(listnum)-1))
    return dev

# make cleaning function:
def clean_outliers(dumbfile: str) -> np.array:
    # fetch all prices, convert to list
    dumblist = []

    with open(dumbfile) as f:
        for tran in f:
            for word in tran.split():
                if word.startswith("price"):
                    dumblist.append(float(word.split("=")[1]))


    # convert list to 1D array
    prize_arr = np.array(dumblist)

    # change invalid prizes in the array (by using deviation function) with mean value of the array

    for num in prize_arr:
        if (num - np.mean(prize_arr)) < 3*deviation(prize_arr):
            num == np.mean(prize_arr)


# write out dumblist
#print(clean_outliers("data/2026/library_cafe/POS_02/register_sales.log"))




