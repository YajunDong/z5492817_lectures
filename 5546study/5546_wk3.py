# the white space standard in Python is 4 spaces

# evaluate to True if the string 'a' is in the set s or if 'b' is not in the set s
s = {'z'}
print(not ('a' not in s and 'b' in s))
print('a' in s or 'b' not in s)
print('a' in s or not 'b' in s)

# loop
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for item in l:
    if not item.startswith("Forest"):
        print(item)
for index, suburb in enumerate(l):
    print(f"{index}: {suburb}")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FIZZ BUZZ")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(i)

first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
for last_name in last_names:
    for first_name in first_names:
        for middle_name in middle_names:
            if middle_name is None:
                full_name = f"{first_name} {last_name}"
            else:
                full_name = f"{first_name} {middle_name} {last_name}"
            print(full_name)

numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
# way 1
temp_largest = numbers[0]
print('before', temp_largest)
for number in numbers:
    if number>temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest number if {temp_largest}')
# way 2
largest = max(numbers)
print(f'The largest number is {largest}')

# while loops
the_sum = 0
i = 1
while i <= 100:
    the_sum = the_sum + 1
    i = i + 1
print(the_sum)

for i in range(1,4):
    for j in range(1,4):
        if  i <= j:
            print(i,j)

# continue
the_sum = 0
for i in range(1,101):
    if i % 2 != 0 and i % 3 != 0 and i % 7 != 0 and i % 13 !=0:
        print(f'    the_sum is {the_sum}')
        the_sum = the_sum + i
print(f'Sum is {the_sum}')

# break
fib_current = 1
fib_prior = 0
while True:
    print(f'Fibonacci value is {fib_current}')
    fib_current, fib_prior = fib_current + fib_prior, fib_current
    if fib_current >= 10000:
        break
print(f'First Fibonacci value greater than 10,000 is {fib_current}')

# break and continue
for x in range(0, 4):
    print(f"Outer loop: x = {x}")
    for y in range(0,4):
        print(f"Start of Inner loop: y = {y}")
        if y > x:
            print(f"y = {y} > x = {x}, breaking out of inner loop")
            break
        elif x + y >= 4:
            print(f"x = {x} and y ={y} have sum >= 4, continuing to next y value")
            continue
        elif (x + y) % 2 != 0:
            print(f"x = {x} and y = {y} have non-even sum, continuing to next y value")
            continue
        print(f"x = {x} and y = {y} have even sum less than 4")

for odd in range(1, 10, 2):
    for even in range(0, 10, 2):
        if even > 2:
            break
    print(even, odd)

for even in range(0, 10, 2):
    if even > 2:
        continue
    print(even)

# if
number = int(input('What is your favourite number? '))
if number == 42:
    print('That is my favourite number too!')
print('Good bye')

# if + else
number = int(input('What is your favourite number? '))
if number == 42:
    print('That is my favourite number too!')
else:
	print('That is not my favourite number.')

# if + elif + else
number = int(input('What is your favourite number? '))
if number == 42:
    print('That is my favourite number too!')
elif number == 21:
    print('That is my second favourite number')
else:
    print('That is neither of my favourite numbers.')

number = int(input('What is your favourite number? '))
if number == 42: print('That is my favourite number too!')
elif number == 21: print('That is my second favourite number')
else: print('That is neither of my favourite numbers.')

# Nesting
number = int(input('What is your favourite number? '))
if number > 10:
    print('That is a big number')
    if number > 100:
        print('It is bigger than 100')
print('Good bye')

#While
# Sometimes you might want to repeat a set of statements for as long as a certain condition is true. For this you can use a while statement.
# 1
n = 1
while n <= 10:
    print(n)
    n = n + 1
print('Finished')

# 2
n = 1
while n <= 10:
    if n % 2 == 0:
        print(n)
    n = n + 1
print('Finished')

# 3
string = 'The quick brown fox jumped over the lazy dog'
occurrences = 0
i = 0
while i < len(string):
    if string[i] == 'e':
        occurrences += 1
    i += 1
print("The letter 'e' occurs", occurrences, "times")
# The letter 'e' occurs 4 times

# 4
i = 0
while i < 10:
    i += 1
    if i == 5:
	    continue
    print(i)
print('Finished')

#breaking 5
i = 0
while i < 10:
    i += 1
    if i == 5:
	    break
    print(i)
print('Finished')

# You can get it to do this by adding a while loop, with a condition that always evaluates to true:
# 6
while True:
    name = input('What is your name? ')
    print('Hello', name)

# 7
while True:
    name = input('What is your name? (Enter x to stop) ')
    if name == 'x':
        break
    print('Hello', name)

#loop
#Looping over tuples is just the same as looping over lists.
for v in ("string", True, 1):
    print(v)
'''
string
True
1
'''

#Dictionaries
#depending on whether you want to loop over (a) keys, (b) values or (c) both keys and values simultaneously
d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key in d:
    print(key)

for val in d.values():
    print(val)

for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")

for key, value in d.items():
    print(f'KEY: {key} VALUE: {value}')

#Ranges
# omitting the `step` parameter
for i in range(0, 5):
    print(f"i is now {i}")
for i in range(5):
    print("i is now {}".format(i))
'''
i is now 0
i is now 1
i is now 2
i is now 3
i is now 4
'''
# Explicitly setting the `step` parameter to 1
for i in range(0, 5, 2):
    print(f"i is now {i}")
for i in range(0, 5, 2):
    print("i is now {}".format(i))
'''
i is now 0
i is now 2
i is now 4
'''

for i in range(5,0):
    print("This will not execute because start is greater than stop.")
for i in range(5,0,-1):
    print("This message will self-destruct in {} ".format(i))
'''
This message will self-destruct in 5 
This message will self-destruct in 4 
This message will self-destruct in 3 
This message will self-destruct in 2 
This message will self-destruct in 1 
'''

letters = ["a", "b", "c", "d", "e"]
print(f"letters = {letters}")
i = 0
for x in letters:
    print(f"letters[{i}] --> {x}")
    i += 1
'''
letters = ['a', 'b', 'c', 'd', 'e']
letters[0] --> a
letters[1] --> b
letters[2] --> c
letters[3] --> d
letters[4] --> e
'''

letters = ["a", "b", "c", "d", "e"]
for tup in enumerate(letters):
    print(tup)
'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
'''
for i, x in enumerate(letters):
    print(f"letters[{i}] --> {x}")
'''
letters[0] --> a
letters[1] --> b
letters[2] --> c
letters[3] --> d
letters[4] --> e
'''

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for i, tup in enumerate(d.items()):
    print(f'Iteration {i} gives {tup}')
'''
Iteration 0 gives ('beauty', True)
Iteration 1 gives ('truth', True)
Iteration 2 gives ('red wheelbarrow', 100000)
Iteration 3 gives (5, 'fingers')
'''
for i, tup in enumerate(d.items(), start=1000):
    print(f'Iteration {i} gives {tup}')
'''
Iteration 1000 gives ('beauty', True)
Iteration 1001 gives ('truth', True)
Iteration 1002 gives ('red wheelbarrow', 100000)
Iteration 1003 gives (5, 'fingers')
'''

# to sum up the integers less than or equal to 100
# 1
the_sum = 0
for i in range(1,101):
   the_sum = the_sum + i
print(the_sum)
# 2
the_sum = 0
i = 1
while i <= 100:
    the_sum = the_sum + i
    i = i + 1
print(the_sum)

# for nesting with if
sum_of_evens = 0
for i in range(1,101):
    if i % 2 == 0: # i is even
        sum_of_evens = sum_of_evens + i
print(f'Sum of evens is {sum_of_evens}') # Sum of evens is 2550

years = [2018, 2019, 2020]
months = [
    "Jan",
    "Feb",
    "Mar",
     ]
for year in years:
   for month in months:
       print("Year: {}, Month: {}".format(year, month))
'''
Year: 2018, Month: Jan
Year: 2018, Month: Feb
Year: 2018, Month: Mar
Year: 2019, Month: Jan
Year: 2019, Month: Feb
Year: 2019, Month: Mar
Year: 2020, Month: Jan
Year: 2020, Month: Feb
Year: 2020, Month: Mar
'''

# loop over the elements and print their values.
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for item in l:
    print(item)
#Using the provided list l, loop over the elements.
#However, only print them if they do not begin with the letters "Forest".
#Use an if statement. You may extract letters from a string using a slice.
for item in l:
    if not item.startswith("Forest"):
        print(item)

#Using the Dictionary provided, print out the town and population for each of the suburbs beginning with f meeting the following criteria:
#The suburb's name does not begin with "Forest"
#The population data exists. This means that the population is not None.
#In fact, is not None is how you test for that a value is not None in Python. Smart!
#Each line in the output should look like SUBURB_NAME: POPULATION.
#So, for example, Fairfield would be:
#Fairfield: 18081
f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for suburb, population in f_suburbs.items():
    if suburb.startswith("Forest") or population is None:
        continue
    print(f"{suburb}: {population}")
'''
Fairfield: 18081
Fairfield East: 5273
Fairfield Heights: 7517
Fairfield West: 11575
Fairlight: 5840
Fiddletown: 233
Five Dock: 9356
Freemans Reach: 1973
Frenchs Forest: 13473
Freshwater: 8866
'''

#Look over all integers from 1 to 100, doing the following:
#If the integer is divisible by 3 (but not by 5), write its value and Fizz. e.g., 12: Fizz
#If the integer is divisible by 5 (but not by 3), write its value and Buzz, e.g., 25: Buzz
#If the integer is divisible by 3 and divisible by 5, write its value and FIZZ BUZZ (in caps), e.g. 15: FIZZ BUZZ
#If none of the above apply, simply print the integer value
#To check if an integer j is divisible by 3, for example, use the logical expression j % 3 == 0.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FIZZ BUZZ")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(i)

#Using the provided list l, loop over the elements and print their positional index and value.
#The print format should be POSITIONAL_INDEX: SUBURB.
#So, Fairfield would look like:
#0: Fairfield
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for index, suburb in enumerate(l):
    print(f"{index}: {suburb}")
'''
0: Fairfield
1: Fairfield East
2: Fairfield Heights
3: Fairfield West
4: Fairlight
5: Fiddletown
6: Five Dock
7: Flemington
8: Forest Glen
9: Forest Lodge
10: Forestville
'''


#This condition will only fail under certain conditions: the value of happy is 0, None, False, and empty string or list, etc...
happy = 0
if happy is True:
    print("I am happy")