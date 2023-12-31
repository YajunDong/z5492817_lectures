# 1
import os   # os provides a way to use operating system-dependent functionality, such as reading or writing files

def safe_open(pth, mode='rt'):
    if 'w' in mode:   # check whether file opened for writing
        if os.path.exists(pth):   # check whether file in path (pth)
            with open(pth, 'r') as file:    # Opens the specified file in read-only ('r') mode and assigns it to File.
                # Use the with statement to ensure that the file is properly closed after reading.
                content = file.read()   # Reads the contents of the file and stores them in a variable called content
            if len(content) > 0:   # if yes, means file has some content
                raise Exception
    return open(pth, mode)   # If the above conditions are not met, this line opens the file specified by pth
    # with the given mode (e.g., 'r', 'w', 'a') and returns the corresponding file object.

if __name__ == "__main__":     # Check that the script is run as a main program (not imported as a module)

    # Opening an existing file with content for reading
    with safe_open("test_file_exists_with_content.txt", mode='r') as fobj:
       print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("test_file_exists_no_content.txt", mode='w') as fobj:
       fobj.write('content')

    # Opening an existing file with content for writing - should raise Exception
    with safe_open("test_file_exists_with_content.txt", mode='w') as fobj:
       fobj.write('content')

# 2  # pd.series(data=[],index=[])
import pandas as pd

# Part (a)
# Create a pandas series called series_abc with
# index ['a', 'b', 'c'] and values [1, 2, 3]
series_abc = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Part (b)
# Given the stock price-date dictionary prc_date
# listed below, create a pandas series series_stk
# with the dates as indices and the prices as values.
prc_date = {
    7.1600: '2020-01-02',
    7.1900: '2020-01-03',
    7.0000: '2020-01-06',
    7.1000: '2020-01-07',
    6.8600: '2020-01-08',
    6.9500: '2020-01-09',
    7.0000: '2020-01-10',
    7.0200: '2020-01-13',
    7.1100: '2020-01-14',
    7.0400: '2020-01-15',
    }
series_stk = pd.Series(prc_date.keys(), index=prc_date.values())

# Part c
# Given the dictionary
dic = {i:i+1 for i in range(10000)}
# create a Pandas series called series_ones
# with indices from 0 through 9999 and with
# all values equal to 1.
# Do not use a secondary dictionary to create the series in Pandas.
# Instead, specify the data and index arguments directly.
series_ones = pd.Series(data=[1] * 10000, index=range(10000))

# 3
""" main.py
Code challenge
"""
import numpy as np
import pandas as pd
# import yfinance as yf # Uncomment this line if you are wish to work with `yfinance` outside of Ed

# Write this function
def fx_code(from_cur, to_cur):
    """ Creates a string with the ticker required to download exchange rates
    using yfinance. The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`.

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced.

    to_cur : str
        The ISO code of the currency with the value of one unit of `from_cur`.

    Returns
    -------
        A string that meets the `yfinance` ticker standards with ALL characters in upper case.
        The function should also be able to ignore leading and trailing spaces. For example,
        " aud", "Aud ", and " AUD " all are treated as "AUD" internally. See the
        Notes section below for more information.

    Notes
    -----
    Yahoo finance uses the following naming rules to define the ticker of the
    exchange rate AAA/BBB:
    usd/aud

    1. If AAA is the USD, then the ticker is "BBB=X", i.e., the second currency
       code with "=X" added at the end.
    2. If AAA is not the USD, then the ticker is "AAABBB=X"

    For example, the ticker for AUD/USD is "AUDUSD=X", while the ticker for
    USD/AUD is "AUD=X"

    So, if `from_cur=AAA` and the `to_cur=BBB`, the YF ticker will be:
    1. "BBB=X" if AAA is USD
    2. "AAABBB=X" if AAA is not the USD
    """
    from_cur = from_cur.strip().upper()   # strip(): Deletes the Spaces. upper(): all uppercase letters
    to_cur = to_cur.strip().upper()
    # `from_cur=AAA` and the `to_cur=BBB`
    if from_cur == 'USD':    # if AAA is USD
        ticker = f"{to_cur}=X"    # if yes >>> "BBB=X"
    else:   # 否则
        ticker = f"{from_cur}{to_cur}=X"   # "AAABBB=X"
    return ticker
    pass

# get_fx is provided to demonstrate how you can download currency data from `yfinance`.
# Once your fx_code function above is correct, get_fx should work on a computer
# that has the `yfinance` package installed.
def get_fx(from_cur, to_cur, period=None, interval=None):
    """ Downloads the exchange rate between the `from_cur` and the `to_cur`.
    The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced

    to_cur : str
        The ISO code of the currency with the value of one unit of
        `from_cur`.

    period : str, None
        valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        (optional, default is '1mo')

    interval : str, None
        valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        (optional, default is '1d')

    Returns
    -------
    df
        Dataframe with daily exchange rates from Yahoo Finance

    """
    # Defaults
    if period is None:
        period = '1mo'
    if interval is None:
        interval = '1d'

    tic = fx_code(from_cur, to_cur)

    # fetches the data
    df = yf.download(tic, period=period, interval=interval)

    return df


# 4
import pandas as pd
import numpy as np
from unanswered import *

aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = pd.Series(data=[val for date, val in aud_usd_lst], index=[date for date, val in aud_usd_lst], name='AUD/USD')
# [val for date, val in aud_usd_lst] = pick val from 遍历date and value in 列表aud_usd_lst
eur_aud_series = pd.Series(data=[val for date, val in eur_aud_lst], index=[date for date, val in eur_aud_lst], name='EUR/AUD')
df = pd.concat([aud_usd_series, eur_aud_series], axis=1)
# used to concatenate or combine Pandas DataFrames or Series along a particular axis (either rows or columns)
# It's a powerful tool for combining data from different sources into a single structure for further analysis.
# axis=0, concatenation occurs along rows (stacking data vertically).
# axis=1, concatenation occurs along columns (combining data horizontally).

# 5
import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    date_df = pd.DataFrame(date_info, columns=['row_id', 'Date'])
    # date_info and contains two columns: 'row_id' and 'Date'.
    aud_usd_df = pd.DataFrame(aud_usd_info, columns=['row_id', 'AUD/USD'])
    eur_aud_df = pd.DataFrame(eur_aud_info, columns=['row_id', 'EUR/AUD'])
    combined_df = date_df.merge(aud_usd_df, on='row_id', how='outer').merge(eur_aud_df, on='row_id', how='outer')
    # Created by merging these three dataframes on the "row_id" column with "external,"
    # ensuring that all unique "row_id" values are included in the generated DataFrame
'''.merge()
    right: The DataFrame you want to merge with the calling DataFrame.
    how: Specifies how the merge operation should be performed. It can take values like: 'inner','outer''right''left'
    on: The column(s)
    left_on and right_on: These parameters allow you to specify different column names
    suffixes: If there are columns with the same name in both DataFrames (
    validate: You can use this parameter to ensure'''
    combined_df.set_index('Date', inplace=True)
    # .set_index('Date') set a specific column as the index of the DataFrame
    # The inplace parameter is set to True, which means that the changes should be applied directly to the existing DataFrame combined_df.
    # If inplace is set to False or not provided (by default), the operation returns a new DataFrame indexed by the "date" column, leaving the original DataFrame unchanged.
    # retrieve data associated with the date "2020-09-08" with combined_df.loc['2020-09-08']
    combined_df.sort_index(inplace=True)
    # Make sure the dates are in ascending order
    combined_df = combined_df[['AUD/USD', 'EUR/AUD']]
    # The DataFrame is reorganized to contain only "AUD/USD" and "EUR/AUD" columns
    return combined_df


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)