# df.loc & df.iloc
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
df.set_index('Name', inplace=True)   # set name as index
value = df.loc['Alice', 'Age']
print(value)
subset = df.loc[['Alice', 'Charlie'], ['Age', 'City']]
print(subset)
slice = df.loc['Bob':'Charlie', 'Age':'City']
print(slice)
value = df.iloc[0, 1]
print(value)
subset = df.iloc[[0, 2], [0, 2]]
print(subset)
slice = df.iloc[1:3, 1:3]
print(slice)


def mean_by_type(df):
    """ Example:
    If the data frame is
            type  A  B  C
        idx
        0      x  1  0  1
        1      x  0  0  1
        2      y  1  0  1

    This function will return:
                A    B    C
        type
        x     0.5  0.0  1.0
        y     1.0  0.0  1.0
    """
    # <COMPLETE THIS PART>
    result = df.groupby('type').mean()
'''
1. `df` is a DataFrame: data is organized into rows and columns.
2. `df.groupby('type')`: a new DataFrame by grouping the original DataFrame based on the 'type' column. 
3. `.mean()`: calculates the mean (average) value of each numeric column within each group. 
This results in a DataFrame where each row corresponds to a unique value in the 'type' column,
and the columns represent the mean values of the numeric columns for each group.
'''
    return result


def last_by_type_v0(df):
    """ Returns a data frame with the last "row" of DF for each unique value of the column "type".
    The last row is defined as the row with the largest index value (if DatetimeIndex, the row with the most recent index value).

    Example
    If the data frame is
            type  A  B  C
        idx
        0      x  1  0  1
        1      x  0  0  1
        2      y  1  0  1

    This function will return the following data frame:
              A  B  C type
        type
        x     0  0  1    x
        y     1  0  1    y    """
    # <COMPLETE THIS PART>
    last_rows = df.groupby('type').apply(lambda group: group[group.index == group.index.max()])
    # apply is used to apply a function to each group.
    # group.index represents the index of the current group, and group.index.max() finds the maximum index value within that group.
    last_rows.set_index('type', inplace=True)   # sets the 'type' column as the index of the last_rows DataFrame
    last_rows['type'] = last_rows.index   # adds a new column 'type' to the last_rows DataFrame.
    # This is done by assigning the index of last_rows (which is the 'type' values) to the 'type' column.
    return last_rows

'''   group[group.index == group.index.max()]   e.g. 
   type  value
0     A      1
1     A      2
2     B      3
3     B      4
4     B      5
For the 'A' group:
group.index represents the indexes (row numbers) of the 'A' group, which are [0, 1].
group.index.max() calculates the maximum index within the 'A' group, which is 1.
group[group.index == group.index.max()] selects the row in the 'A' group where the index matches the maximum index, which is row 1.
For the 'B' group:
group.index represents the indexes (row numbers) of the 'B' group, which are [2, 3, 4].
group.index.max() calculates the maximum index within the 'B' group, which is 4.
group[group.index == group.index.max()] selects the row in the 'B' group where the index matches the maximum index, which is row 4.
  type  value
1    A      2
4    B      5
'''

""" main.py


"""

import pandas as pd

import utils


def last_by_type_v1(df):
    """ Returns a data frame with the last "row" of DF for each unique
    value of the column "type" AND a column called "org_index" with the value
    of the index in the original data frame associated with this row.
        The last row is defined as the row with the largest index value within
    each group (if DatetimeIndex, the row with the most recent index value).
        Example
    If the data frame is
            type  A  B  C
        idx
        0      x  1  0  1
        1      x  0  0  1
        2      y  1  0  1
    This function will return:
             type  A  B  C org_index
        type
        x       x  0  0  1         1
        y       y  1  0  1         2
    """
    # <COMPLETE THIS PART>
    last_rows = df.groupby('type').apply(lambda group: group[group.index == group.index.max()])
    last_rows.set_index('type', inplace=True)
    last_rows['type'] = last_rows.index
    last_rows['org_index'] = df.groupby('type').apply(lambda group: group.index.max())
    return last_rows

'''
1. last_rows = df.groupby('type').apply(lambda group: group[group.index == group.index.max()])
2. last_rows['org_index'] = df.groupby('type').apply(lambda group: group.index.max())
The first code generates a new DataFrame with only the latest rows within each group from the original DataFrame df.
The second code adds an 'org_index' column to the last_rows DataFrame, 
indicating the maximum index value (latest index) for each group in the original DataFrame df.
the key difference is that the first code snippet filters the rows to retain only the latest rows, 
while the second code snippet calculates the maximum index value for each group 
and adds it as an 'org_index' column to the original rows without filtering.
'''
def fuzzy_colnames(df):
    """
        1. Reverse the string (e.g., column "ABC" becomes "CBA").
        2. If the column label includes the (upper case) letter "B", we have
        two cases:
            a. If the (lower case) letter "b" is NOT in the column name,
            reverse the case of any occurrence of "B" (so each upper case "B"
            will become lower case "b").
            b. If the column name also includes the (lower case) letter "b", do
            nothing.

            For example:
            - "CBA" becomes "CbA"
            - "ZbB" does not change (because name includes a lower case "b')
            - "BBa" becomes "bba"
            - "ZZZ" does not change
    Example
    If the data frame `df` is:
             ABC  Xxb  zy  Bxb
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    This function will return the following data frame:
             CbA  bxX  yz  bxB
        idx
        0      1    0  10   20
        1      0    0  11   21
        2      1    0  12   22

    Note: The order of the columns does not matter

    """
    # <COMPLETE THIS PART>
    modified_cols = []  # initializes an empty list
    for col in df.columns:  # iterates over col, representing the current column name in df
        reversed_col = col[::-1]  # Reverse the column name
        # checks whether the reversed column name reversed_col contains the upper case letter "B"
        # and does not contain the lower case letter "b"
        if "B" in reversed_col and "b" not in col:
            # Replace all upper case "B" with lower case "b"
            modified_col = reversed_col.replace("B", "b")
        else:
            modified_col = reversed_col
        modified_cols.append(modified_col)  # add reversed column name to the modified_cols list.
    modified_df = df.copy()  # Create a new DataFrame with modified column names
    modified_df.columns = modified_cols
    return modified_df



def fuzzy_values(df):
    """ Replaces the values in THE FIRST column of the data frame `df` according to
    the following criteria (IN THIS ORDER):
    1. If the value is a number between 0 and 0.5 (so 0 <= value <= 0.5),
    replace this value with the sum of the values of all columns in this row.
    2. If the value is between 1.0 and 2.0 (so 1.0 <= value <= 2.0), replace
    this value with -99.
    Important: The order matters! For instance, if in part 1. the original
    value is 0.1 and the sum of all columns (in that row) is 1.5, this value
    will be then replaced by -99 in part 2.

    Example
    If the data frame `df` is:
                A      B
        idx
        0     0.4    1.0
        1     0.0    0.5
        2    10.0    0.0
        3     1.5 -100.0
        4     0.1    0.1
        5     0.5  -10.0

    This function will return the following data frame:
                A      B
        idx
        0   -99.0    1.0
        1     0.5    0.5
        2    10.0    0.0
        3   -99.0 -100.0
        4     0.2    0.1
        5    -9.5  -10.0       """
    # <COMPLETE THIS PART>
    for idx, value in enumerate(df.iloc[:, 0]):
        if 0 <= value <= 0.5:   # If the value is a number between 0 and 0.5,
            new_value = df.iloc[idx].sum()   # the sum of the values of all columns in this row
            df.iloc[idx, 0] = new_value    # replace this value with the sum of the values of all columns in this row.
        elif 1.0 <= value <= 2.0:   # If the value is between 1.0 and 2.0
            df.iloc[idx, 0] = -99   # replace this value with -99
    return df
'''   
df.iloc[idx]
df: It is the DataFrame you want to work with.
.iloc: It's an indexer for DataFrame, which is used to access rows and columns by integer location.
idx: It's an integer that specifies the row's location you want to access.
For example, if you have a DataFrame named df and you want to access the 3rd row, you would use df.iloc[2]. 
This would give you a Series containing the data from the 3rd row of the DataFrame.

df.iloc[idx, 0]
0: It's an integer that specifies the column's location you want to access.

df.iloc[:, 0]
[:, 0]: These indices indicate that you want to select all rows (:) and the first column (0) of the DataFrame.

The enumerate function is used to iterate over the elements of a sequence (such as a list, an array, or in this case, 
the values of a specific DataFrame column) while keeping track of both the elements and their corresponding indices. 
'''
