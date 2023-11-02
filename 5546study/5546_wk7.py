'''
<target> = <expression>
1. read from left to right >>> if <target> is valid, if not >> exception
2. evaluate <expression>, produce an object (instance stored in the computer memory)
3. assign the object produced by <expression> to the variable >> the variable is now bound to that object
'''
import pandas as pd
import numpy as np
import copy

lst0 = [1,2]
lst1 = [2,3]
lst2 = lst0   # this 2 have same ID
print(lst2)
lst2[0] = -99
print(lst2)
print(lst0)

# here is 4 list
lst0 = [1,2]
lst1 = [3,[1,2]]
lst2 = [3,lst0]
lst2[1][0] = -99
print(lst0,lst1,lst2)

# copy.copy & copy.deepcopy
original_list = [1, [2, 3]]   # Original list with nested lists
shallow_copy_list = copy.copy(original_list)   # Shallow copy using copy.copy
deep_copy_list = copy.deepcopy(original_list)   # Deep copy using copy.deepcopy
# Modify the shallow copy
shallow_copy_list[0] = 99
shallow_copy_list[1][0] = 88
# Modify the deep copy
deep_copy_list[0] = 77
deep_copy_list[1][0] = 66
print("Original List:", original_list)  # Output: [1, [88, 3]]
print("Shallow Copy:", shallow_copy_list)  # Output: [99, [88, 3]]
print("Deep Copy:", deep_copy_list)  # Output: [77, [66, 3]]
# If a completely independent copy is required, copy.deepcopy should be used.
# If you only need to copy the structure of the original object,
# but do not need to copy the reference relationships of its internal elements, you can use copy.copy

# series.loc & series.iloc
'''
series.loc:
Uses label-based indexing: loc method uses label indexing, meaning you can select data by label names.
Inclusive of the end position: loc method is inclusive of the end position, which means the selected range includes both the start and end positions.
Suitable for non-integer labels: loc method can be used with non-integer labels, such as string labels.
Syntax: series.loc[start_label : end_label]
'''
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
result1 = data.loc['B':'C']  # Select data between labels 'B' and 'C'
print(result1)
'''
series.iloc:
Uses integer-based position indexing: iloc method uses integer positions to index the data, allowing you to select data by position.
Exclusive of the end position: iloc method is exclusive of the end position, which means the selected range includes the start position but excludes the end position.
Primarily used for integer indices: iloc method is primarily used with integer indices, such as the default integer index 0, 1, 2, ...
Syntax: series.iloc[start_position : end_position]
'''
data = pd.Series([10, 20, 30, 40])
result2 = data.iloc[1:3]  # Select data between positions 1 and 2
print(result2)


# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)
# Q1: What expression for `sel_q1` below will produce a DATA FRAME
# with the following information?
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-14 | 0.7281  |  NaN    |
# NOTE: replace `put_your_answer_here`
sel_q1 = ['2020-09-08', '2020-09-14']
q1 = df.loc[sel_q1]
# Q2: What expression for `start`, `stop` below will produce a DATA FRAME with
# following output?  (first two rows of `df`)
#
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
(start_q2, stop_q2) = (0, 2)
q2 = df.iloc[start_q2:stop_q2]
# Q3: What expression for `start`, `stop` below will produce a DATA FRAME
# with following output?  (first two rows of `df`)
# |            | AUD/USD | EUR/AUD |
# +------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
(start_q3, stop_q3) = (0, 2)
q3 = df[start_q3:stop_q3]
# Q4: What expression for row_sel, col_sel below will produce a DATA FRAME
# with the following information?
# |            | AUD/USD |
# +------------+---------|
# | 2020-09-08 | 0.7280  |
# | 2020-09-09 | 0.7209  |
row_sel_q4 = ['2020-09-08', '2020-09-09']
col_sel_q4 = ['AUD/USD']
q4 = df.loc[row_sel_q4, col_sel_q4]