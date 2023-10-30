def process_string(s):
    words1 = s.split()
    words1 = [words.lower() for words in words1]
    return words1
print(process_string("This is my test String"))

def process_string(s):
    words = s.split()
    modified_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            modified_words.append(word.lower())
        else:
            modified_words.append(word.upper())
    return modified_words
print(process_string("This is my test String"))

def fizz_buzz_sumz(i):
    total_sum = 0
    for x in range(1, i + 1):
        if x % 3 == 0 and x % 5 == 0:
            continue
        elif x % 3 == 0:
            total_sum += 3 * x
        elif x % 5 == 0:
            total_sum += 5 * x
        else:
            total_sum += x
    return total_sum
result = fizz_buzz_sumz(10)
print(result)

prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}
sorted_keys = [key for key in sorted(prc_dic)]
prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15', None)

'''
import os
import toolkit_config as cfg
import yf_example2
def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.

    Args:
        year (int): The year for which to download stock prices.

    Returns:
        None
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    data = yf_example2.yf_prc_to_csv("QAN.AX", start_date, end_date)
    output_file = f"qan_prc_{year}.csv"
    output_path = os.path.join(cfg.DATA_FOLDER, output_file)
    data.to_csv(output_path, index=False)
if __name__ == "__main__":
    qan_prc_to_csv(2020)
'''

print("The copyright symbol is: \u00A9")
print("The copyright symbol has Unicode hex value: \\u00A9")

list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,26,30,31]
def even_number(lis):
    evennumber = []
    for i in lis:
        if i % 2 == 0:
            evennumber.append(i)
    return evennumber
if __name__ == "__main__":
    lis = list
    print(even_number(lis))

# dic[key] = value
# for key,value in dict.items()

lst = [2,3,10,14,20,21,25,13,15]
new_lst = [x**2 for x in lst if x**2>150]
print(new_lst)

num = [0,1,1,2,5,6,8,2,4,6,8]
result = [x for x in set(num) if x % 2 == 0]  # set：unique
result.sort()   # sort the list
print(result)

def say_hello(name):
	print('Hello,', name)
say_hello('James')   # Hello, James

def say_hello(name = 'James'):
	print('Hello,', name)
say_hello() # The default value will be used   Hello, James
say_hello('Sarah') # The default value will not be used   Hello, Sarah

def say_hello(name = None):
    if name is None:
        print('No name was provided')
    else:
        print('Hello,', name)
say_hello()   # No name was provided
say_hello('Sarah')   # Hello, Sarah

def ends(string):
    first_char = string[0]
    last_char = string[-1]
    return first_char, last_char
print(ends('Australia'))   # ('A', 'a')
print(ends('Australia')[0])   # A
print(ends('Australia')[1])   # a

def divide(numerator, denominator, num_places):
	return round(numerator/denominator, num_places)
# Not clear which number is which, and order matters:
print(divide(5, 6, 3))   # 0.833
print(divide(3, 6, 5)) # Different result # 0.5
# Clear which number is which, and order doesn't matter:
print(divide(numerator = 5, denominator = 6, num_places = 3))    # 0.833
print(divide(num_places = 3, denominator = 6, numerator = 5)) # Same result  # 0.833

# Allowing an arbitrary number of arguments
def smallest(numbers): # Expects numbers to be a list
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest
print(smallest([42, 12])) # Provide a single list of 2 numbers # 12
print(smallest([4, 11, 15, 2, 3])) # Provide a single list of 5 numbers # 2

x = 3 # Globally defined x
def my_func():
    x = 5 # Locally defined x - changes to this x will not be reflected outside the function
my_func() # even calling my_func() will not change the global x variable.
print(x) # Calls print on the global x variable. # x = 3

x = 3
def my_func(y):  # y is a locally defined variable
    return y+2   # make the changes to y and pass them back as the return value
x = my_func(x) # This will update the globally defined variable x
print(x) # x = 5

def acronym(string):
    result = ''
    words = string.split(' ')
    def upper_first(string):
        return string[0].upper()
    for word in words:
        result += upper_first(word)
    return result
print(acronym('World Health Organisation'))   # WHO

def last_letter(name):
    return name[-1]
names = ['Geoff', 'Kim', 'Louise', 'Tam', 'Helen']
names.sort(key=last_letter) # Use the function defined above
print(names)   # ['Louise', 'Geoff', 'Kim', 'Tam', 'Helen']

names = ['Geoff', 'Kim', 'Louise', 'Tam', 'Helen']
names.sort(key=lambda name: name[-1]) # No need to define a function in advance
print(names)   # ['Louise', 'Geoff', 'Kim', 'Tam', 'Helen']

# Lambda functions can have more than one parameter:
lambda a, b: a + b

def add(x, y):
	return x + y
def subtract(x, y):
	return x - y
def apply(f, x, y):
	return f(x, y)
print(apply(add, 10, 1))   # 11
print(apply(subtract, 10, 1))   # 9

def add1(x):
	return x + 1
def subtract1(x):
	return x - 1
def compose(f, g):
	return lambda x: f(g(x))
add2 = compose(add1, add1)
print(add2(10))   # 12
do_nothing = compose(add1, subtract1)
print(do_nothing(10))   # 10

# Recursion
# factorial
# WAY 1
def factorial(n):
	result = 1
	for x in range(1, n+1):
		result *= x
	return result
number = int(input('Enter a number: ')) # Must convert the input to an integer
print('The factorial of', number, 'is', factorial(number))
# WAY 2
def factorial(n):
	if n == 0:
		return 1
	return n*factorial(n-1)
if __name__ == '__main__':
	n = input('Enter a number: ')
	print(f'{n}! = {factorial(int(n))}')
# WAY 3
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) # Recursion - the function calls itself
number = int(input('Enter a number: ')) # Must convert the input to an integer
print('The factorial of', number, 'is', factorial(number))