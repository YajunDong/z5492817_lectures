#seperator
a = 10
print('The value of a', a, sep=' = ')
print('hello', end='\t-\t') # \t is a tab character
print('world', end='.\n') # \n is a newline character

'''
1. List:
    - Mutable: Lists are mutable, which means you can change their content (add, remove, or modify elements) after creation.
    - Ordered: Lists are ordered collections, which means they maintain the order of elements based on their position.
    - Syntax: Lists are created using square brackets `[]`.
    - Example: `my_list = [1, 2, 3, 4]`
2. Tuple:
    - Immutable: Tuples are immutable, which means once you create a tuple, you cannot change its content (add, remove, or modify elements).
    - Ordered: Like lists, tuples are also ordered collections, so they maintain the order of elements.
    - Syntax: Tuples are created using parentheses `()`.
    - Example: `my_tuple = (1, 2, 3, 4)`
3. Set:
    - Mutable (partially)**: Sets are mutable with regard to adding and removing elements. However, the elements themselves must be immutable (e.g., numbers, strings).
    - Unordered: Sets are unordered collections, so they do not maintain the order of elements.
    - Uniqueness: Sets automatically eliminate duplicate elements; each element appears only once in a set.
    - Syntax: Sets are created using curly braces `{}` or the `set()` constructor.
    - Example: `my_set = {1, 2, 3, 4}`
4. Dictionary: (Use a **dictionary** when you need to associate keys with values in an unordered manner, and you want **fast lookups based on keys**)
    - Mutable: Dictionaries are mutable collections that store key-value pairs, where keys are unique and immutable (usually strings or numbers).
    - Unordered: Dictionaries are unordered, meaning they don't guarantee any specific order of key-value pairs.
    - Unique
    - Syntax: Dictionaries are created using curly braces `{}` with key-value pairs separated by colons `:` (e.g., `my_dict = {'name': 'John', 'age': 30}`).
    - Example: `my_dict = {'name': 'John', 'age': 30}`
'''

print(1 + 2)   #3
print(10 - 5)   #5
print(3 * 4)   #12
print(20/4)   #5.0
print((1 + 2)*(3 + 4))   #21
print(10/(3-1))   #5.0
print(10**2) # 10 to the power 2 = 100
print(10//3) # 10 divided by 3 and rounded down = 3
print(-10//3) # -10 divided by 3 and rounded down = -4
print(10 % 3) # The remainder when 10 is divided by 3 = 1
print(1+2*3) # Same as 1 + (2*3) = 7
print(2**3*4) # Same as (2**3) * 4 = 32
print(24/6*2) # Same as (24/6) * 2 = 8.0
print(24/6/2) # Same as (24/6) / 2 = 2.0
print(2**2**3) # Same as 2**(2**3) = 256

print(1 == 1.0)   # True
print(1 is 1.0)   # False

#Floating-point numbers and ==
#Because floating point numbers have limited precision you will experience strange results when attempting to compare them with ==
print(0.1 + 0.2 == 0.3)   # False

# round
print(round(4.5,0))   # 4.0
print(round(5.5,0))   #6.0
print(round(-4.5,0))   #-4.0
print(round(-5.5,0))   #-6.0

print(int('3') + float('2.0')) # Convert strings to numbers and add them = 5.0
print(abs(-5)) # Absolute value of -5 = 5
print(pow(2, 4)) # 2 to the power of 4.  This is the same as ** = 16
print(round(3.567, 2)) # Round 3.567 to 2 decimal places 3.57

'''
# not
not True # --> False
not False # --> True
# and
True and True # --> True
True and False # --> False
False and True # --> False
False and False # --> False
# or
True or True # --> True
True or False # --> True
False or True # --> True
False or False # --> False
'''

import numpy as np
#Parameter Values
S0=100. #initial index level
K=105.  #strike level
T=1.0   #time-to-maturity
r=-0.01 #riskless short rate
sigma=0.38  #volatility
I=100000    #number of simulations
#Valuation Algorithm
z=np.random.standard_normal(I)  #pseudorandom numbers
ST=S0*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*z) #index values at maturity
hT=np.maximum(ST-K,0)   #inner values at maturity
C0=np.exp(-r*T)*np.sum(hT)/I
#Results Output in Console
print("Value of European Call Option is:", round(C0,2))

print("Hi".center(40, '-') )   # --> '-------------------Hi------------------ -'

a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}")
print("The value of a is {} and the value of b is {}".format(a , b))
# The value of a is True and the value of b is 5

# Backslash used to escape a quote mark
print('Penny\'s dog') # Penny's dog

# Backslash used to escape a new line symbol
print('This is one line.\nThis is a second line')
#This is one line.
#This is a second line

# Backslash used to escape a tab symbol
print('Here\tThere')
#Here   There

print('a' * 10) # aaaaaaaaaa

print('A' < 'B')   # True
print('AA' < 'AB')   # True
print('A' < 'AA')   #True

print(len('abcde'))   # 5

# namespaces: Local -> Enclosing (non-global) -> Global -> Built-in -> Qualified

'''- `str.capitalize()` - Returns `str` with the first character uppercase and the rest lowercase
- `str.count()` - Returns the number of times a specified value occurs in `str`
- `str.endswith()` - Returns true if `str` ends with the specified value
- `str.find()` - Searches `str` for a specified value and returns the index at which it is first found (or -1 if it was not found)
- `str.format()` - Returns `str` formatted as specified
- `str.isalpha()` - Returns true if all characters in `str` are from the alphabet
- `str.isdigit()` - Returns true if all characters in `str` are digits
- `str.islower()` - Returns true if all characters in `str` are lower case
- `str.isspace()` - Returns true if all characters in `str`are whitespace characters (i.e. space, tab, or new line)
- `str.isupper()` - Returns true if all characters in `str` are upper case
- `str.lower()` - Returns `str` converted to lower case
- `str.lstrip()` - Returns `str` with whitespace stripped from the left end
- `str.replace(old, new)` - Returns `str` with `old` replaced by `new`
- `str.rfind()` - Searches `str` for a specified value and returns the index at which it is last found (or -1 if it was not found)
- `str.rstrip()` - Returns `str` with whitespace stripped from the right end
- `str.split()` - Splits `str` using a specified delimiter and returns the result as a list
- `str.startsswith()` - Returns true if `str` starts with the specified value
- `str.strip()` - Returns `str` with whitespace stripped from both ends
- `str.title()` - Returns `str` with the first character of each word in upper case
- `str.upper()` - Returns `str` with every character in upper case'''

asx_value = 7111.4
date = "2021-01-25"
units = 1
currency = "AUD"
print("The closing value of", units, "unit of the All Ordinaries on", date, "was",asx_value, currency+".")

# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater
# Use the set f_suburbs as your starting point
f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
specified_suburbs = {
    "Fairfield", "Fairfield East", "Fairfield Heights", "Fairfield West",
    "Fairlight", "Fiddletown", "Five Dock", "Flemington",
    "Forest Glen", "Forest Lodge", "Forestville", "Freemans Reach",
    "Frenchs Forest", "Freshwater"}
f_suburbs = f_suburbs.union(specified_suburbs)
for suburb in f_suburbs:
    if suburb.startswith('F'):
        f_suburbs.add(suburb)
f_suburbs.update(specified_suburbs)
f_suburbs = {suburb for suburb in f_suburbs if suburb.startswith('F')}
for suburb in sorted(f_suburbs):
    print(suburb)

# The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ... where each
# subsequent number is equal to the the preceeding two.
# This means the next elements in the list above would be 8 (5 + 3) and 13 (8 + 5)
# The 9th element in the sequence is 21. Let's call this the `current` value.
# The 8th element in the sequence is 13. Let's call this the `last` Value.
# Using PARALLEL ASSIGNMENT/TUPLE UNPACKING, perform the following operations
# in a single statement
#   1. replace the value of `current` with the value of the 10th
#       element in the sequence (so the sum of the 8th and 9th element)
#   2. replace the value of `last` with the value of the 9th element
current = 21 # at this point, the 9th element of the sequence
last = 13 # at this point, the 8th element of the sequence
# Now, use parallel assignment to replace the value of `current` and `last`
current, last = current + last, current

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs, with the mapping going from suburb keys to population values.
# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866
# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.
# Use the dictionary f_suburbs as your starting point
# Use the dictionary f_suburbs as your starting point
f_suburbs = {
    "Randwick": 29986,
    "Kensington": 15004,
    "Frenchs Forest": 13473,
    "Flemington": None}
# Create a new dictionary to store the filtered and updated suburbs
filtered_f_suburbs = {
    "Fairfield": 18081,
    "Fairfield East": 5273,
    "Fairfield Heights": 7517,
    "Fairfield West": 11575,
    "Fairlight": 5840,
    "Fiddletown": 233,
    "Five Dock": 9356,
    "Flemington": None,
    "Forest Glen": None,
    "Forest Lodge": 4583,
    "Forestville": 8329,
    "Freemans Reach": 1973,
    "Frenchs Forest": 13473,
    "Freshwater": 8866}
# Filter the suburbs that start with 'F' and update the dictionary
filtered_f_suburbs = {key: value for key, value in filtered_f_suburbs.items() if key.startswith('F')}
# Update the original f_suburbs dictionary with the filtered data
f_suburbs = filtered_f_suburbs
# Print the updated dictionary
for suburb, population in sorted(f_suburbs.items()):
    print(f"{suburb}: {population}")

# Use the provided list_a and list_b as your starting point.
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol
list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove('bad')
sol.append('including')
sol.insert(2, 'good')
sol.extend(list_b)

lst = [1, "string", True, None]
print(f"The item at index 0 is {lst[0]}")   # The item at index 0 is 1

lst = ["a", "b", "c", "d", "e", "f"]
print(f"lst[:3] gives {lst[:3]}")   # lst[:3] gives ['a', 'b', 'c']

print(len([1, 2, 3])) # 3 items
print(len(['12', '45'])) # 2 items
print(len([1, 3.14, 'hello', True])) # 4 items
print(len([])) # 0 items

x = ['a', 'b', 'c', 'd', 'e']
print(x[::2]) # Every second element  ['a', 'c', 'e']
print(x[::3]) # Every third element  ['a', 'd']
print(x[::-1]) # Every element in reverse  ['e', 'd', 'c', 'b', 'a']
print(x[::-2]) # Every second element in reverse  ['e', 'c', 'a']

# replacing
x = ['a', 'b', 'c', 'd', 'e']
x[0] = 'z'
print(x)   # ['z', 'b', 'c', 'd', 'e']

#adding
x = ['a', 'b', 'c', 'd', 'e']
x.append('f')
print(x)   # ['a', 'b', 'c', 'd', 'e', 'f']

# insert
x = ['a', 'b', 'c', 'd', 'e']
x.insert(2, 'x')
print(x)   # ['a', 'b', 'x', 'c', 'd', 'e']

# extend
x = ['a', 'b', 'c', 'd', 'e']
y = ['x', 'y', 'z']
x.extend(y)
print(x)   # ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
#or
print(x + y)

# remove
x = ['a', 'b', 'c', 'd', 'e']
print(x.pop(2))   # c
print(x)   # ['a', 'b', 'd', 'e']
print(x.pop())   # e
print(x)   # ['a', 'b', 'd']

x = ['a', 'b', 'c', 'd', 'e']
del x[1]
print(x)   # ['a', 'c', 'd', 'e']

# remove the first item with a given value
x = ['a', 'b', 'c', 'd', 'e', 'c']
x.remove('c')
print(x)   # ['a', 'b', 'd', 'e', 'c']

# remove all items
x = ['a', 'b', 'c', 'd', 'e']
x.clear()
print(x)   # []

# count
x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
print(x.count(7))   # 2

#find the index of the first occurrence of a value
x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]
print(x.index(7))   # 2

print(sum([1, 3, 7, 8, 7, 5, 4, 6, 8, 5]))   # 54

# returns True if all items evaluate to True
print(all([True, True, True]))   # True
print(all(['a', 'a', 'a']))   # True
print(all(['', 'a', 'b']))   # False

# sort the elements of a list by using the sort() method, which orders the items by comparing their values using the < operator.
x = [1, 5, 4, 2, 3]
x.sort()
print(x)   # [1, 2, 3, 4, 5]

x = ['c', 'a', 'e', 'b', 'd']
x.sort()
print(x)   # ['a', 'b', 'c', 'd', 'e']

x = [1, 5, 4, 2, 3]
x.sort(reverse=True)
print(x)   # [5, 4, 3, 2, 1]

x = ['dog', 'chicken', 'mouse', 'horse', 'goat', 'donkey']
x.sort(key=len)
print(x)   # ['dog', 'goat', 'mouse', 'horse', 'donkey', 'chicken']

# For loops
# WAY 1
vowels = ['a', 'e', 'i', 'o', 'u']
i = 0
while i < len(vowels):
    print(vowels[i])
    i += 1

# WAY 2
vowels = ['a', 'e', 'i', 'o', 'u']
for v in vowels:
    print(v)

# break and continue
vowels = ['a', 'e', 'i', 'o', 'u']
print('Everything before o:')
for v in vowels:
    if v == 'o':
        break
    print(v)

print('Everything except o:')
for v in vowels:
    if v == 'o':
        continue
    print(v)

# use the index of an item as well as its value
vowels = ['a', 'e', 'i', 'o', 'u']
for i, v in enumerate(vowels):
	print('The vowel at index', i, 'is', v)

# list of lists
numbers = [[1,2,3],[3,4,5],[6,7,8]]
print(len(numbers))   # 3
print(numbers[0])   # [1, 2, 3]
numbers.reverse()
print(numbers)   # [[6, 7, 8], [3, 4, 5], [1, 2, 3]]

numbers = [[1,2,3],[3,4,5],[5,6,7]]
print(len(numbers[0]))   # 3
print(numbers[0][0])   # 1
numbers[0].reverse()
print(numbers[0])   # [3, 2, 1]

numbers = [[1,2,3],[3,4,5],[5,6,7]]
total = 0
for i in numbers:
    for j in i:
        total += j
print(total)   # 36

lst1 = ['a']
lst2 = ['b', lst1]
lst3 = ['b', ['a']]
print(lst2, lst3) # ['b', ['a']] ['b', ['a']]

lst1 = ['a']
print(f'This is lst1: {lst1}') # This is lst1: ['a']
lst2 = ['b', lst1]
print(f'This is lst2: {lst2}') # This is lst2: ['b', ['a']]
lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}") # This is lst2 after modifying it: ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst2: {lst1}") # This is lst1 after modifying lst2: ['a', 'c']

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")
print(f"This is lst1 after modifying lst3: {lst1}") #This is lst1 after modifying lst3: ['a']

# tuple: keys must be immutable
y = (1, 1, 2, 3, 5, 8)
print(4 in y)  # check # Flase
print(y.count(1)) # 2

x = (1, 2, 3)
y = (4, 5, 6)
z = x + y # Note this will give a tuple
print(z)   # (1, 2, 3, 4, 5, 6)

y = (1, 1, 2, 3)
z = (True, False, True)
print(sum(y))   # 7
print(all(z))   # False
print(any(z))   # True

# set: a set are unordered, which means that they have no index
# Because they are not ordered you can't be sure what order Python will list them in (try running the following snippet multiple times):
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)   # {'o', 'u', 'i', 'a', 'e'}  # each time the result are different

x = {'cat', 'mouse', 'dog', 'cat', 'cat'}
print(x)   # {'cat', 'mouse', 'dog'}  # unique

print(len({'a', 'e', 'i', 'o', 'u'}))   # 5
print(len({}))   # 0

vowels = set()
vowels.add('a')
vowels.add('e')
vowels.add('e') # No error, just not added, because unique
print(vowels)   # {'e', 'a'}

# remove items from a set using the set's remove() or discard() methods. If the item is not in the set then using remove() will cause an error, but using discard() will not:
vowels = {'a', 'e', 'i', 'o', 'u'}
vowels.remove('a')
print(vowels)
vowels.discard('f')   # No error
print(vowels)
# vowels.remove('f')   # Error

vowels = {'a', 'e', 'i', 'o', 'u'}
vowels.clear()   # remove all items from a set
print(vowels)   # set()

# Union of two sets
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}
print(evens | primes)   # {2, 3, 4, 5, 6, 7, 8}
print(evens.union(primes))   # {2, 3, 4, 5, 6, 7, 8}
print(primes.union(evens))   # {2, 3, 4, 5, 6, 7, 8}
print(evens & primes)   # {2}
print(evens.intersection(primes))   # {2}
print(primes.intersection(evens))   # {2}
print(evens - primes)   # {8, 4, 6}
print(evens.difference(primes))   # {8, 4, 6}
print(primes - evens)   # {3, 5, 7}
print(primes.difference(evens))   # {3, 5, 7}

# Dictionary literals are presented in curly braces like set literals
# with key-value pairs separated by commas
# and each key and value separated with a colon.
scores = {'Alice': 0, 'Bob': 1, 'Eve': 2, 'Mallory': 3,}
print(scores)

dictionary = {
    1: 'one',
    'two': 2, # Mixing key types is not good practice as it can lead to confusion
    3: 3}
print(dictionary)   # {1: 'one', 'two': 2, 3: 3}

# uniqueness
scores = {
    'Alice': 0,
    'Alice': 1
}
print(scores)   # {'Alice': 1}

# indexing
scores = {
	'Alice': 0,
	'Bob': 1,
	'Eve': 2,
	'Mallory': 3,
}
print(scores['Alice'])   # 0

# Updating
scores = {
	'Alice': 0,
	'Bob': 1,
	'Eve': 2,
	'Mallory': 3,
}
scores['Bob'] = 900
scores['Alice'] += 1
print(scores)   # {'Alice': 1, 'Bob': 900, 'Eve': 2, 'Mallory': 3}

# Deletion
scores = {
	'Alice': 0,
	'Bob': 1,
	'Eve': 2,
	'Mallory': 3,
}
del scores['Bob']
print(scores)   # {'Alice': 0, 'Eve': 2, 'Mallory': 3}

# iteration
scores = {
	'Alice': 0,
	'Bob': 1,
	'Eve': 2,
	'Mallory': 3,
}
for key in scores:
	print(key)

scores = {
	'Alice': 0,
	'Bob': 1,
	'Eve': 2,
	'Mallory': 3,
}
for key, value in scores.items():
	print(key, value)
