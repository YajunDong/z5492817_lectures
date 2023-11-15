'''
Python is a general purpose programming language
# "py" files containing Python code are called modules.
# A package is a Python module containing other modules.
# A folder containing an _init__.py file is a package.
# Any package is a module but not all modules are packages.

# people split code across Python modules:
# To keep code organised
# To reflect the underlying logic of their program

# Python library: One or more Python modules, which are typically publicly available,
# that collectively create useful tools for programming

# use libraries written by others:
# Doing so eliminates the need to write each part of the program by yourself
# A community of users may be able to help you should you have questions
# Popular libraries are often well tested and robust

# The default order by which Python evaluates code is from top to bottom.

# An object is an actualised version of an instance, and data can vary across objects.
# The instance defines the interactions, called methods, we have with the object.
# e.g. we have a specific “house plan” and want to build houses based on it.
# The house plan is the “class”.
# Then we build physical houses on some residential lands, each of these houses is an “object”.
# And finally, we designate one of those houses to Amy and name it as Amy’s house.  So, Amy’s house is an “instance”

# valid name start with: lower/upper letters, underscores(_)
# valid name includes: lower/upper letters, underscores(_), digits

# When evaluating algebraic calculations, Python follows the PEMDAS rule.
# According to PEMDAS, The precedence of operators is listed below in a high to low manner:
# Parentheses, Exponents, Multiplication and Division, Addition and Subtraction
# And if there are two operations with same precedence in an expression
# the associativity rule will be followed, which means all operators will follow left to right associativity.

# A "Directory" is a basic file storage folder in Pycharm
# but the "Python Package" is a specialized folder marked with  _ _ init_ _.py.

# function & methods
# 1. Functions are independent entities on a Python code, while methods are class dependent.
# 2. Functions are independent of classes, but methods are always defined within a class.
# 3. Functions can be called by their names, while methods should be called using the name of their classes.
# 4. Functions process the data which are passed to them as arguments
# while methods operate the data enclosed in the object of the class to which they are associated.
'''

import yfinance
tic = "Qan.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic,start,end)
df.to_csv('qan_stk_prc.csv')

# convert all the strings in a set to integers
string_set = {"1", "2", "3", "4"}
int_set = {int(s) for s in string_set}
print(int_set)

# 1. variable name can only start with letter and _
# 2. str and int
print(str(1))
a = int(1) + int(2)
print(a)
print(5^2)
print(5**2)
# bool must with True or False, not true or false

