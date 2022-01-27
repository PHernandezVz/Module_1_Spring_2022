"""
Program: cast_to_integer.py
Author: Patricia Hernandez-Vasquez
Last date modified: 01/26/2022

The purpose of this program is to accept any input,
convert to an integer type and output the integer.
"""

# input any value, assigning to a variable
any_value = float(input('Please enter any value: '))

# cast value to an integer
value_as_an_integer = int(any_value)

# print the value as integer
print(int(value_as_an_integer))

# print(type(int(value_as_an_integer))), use to see type of output

# Input   Expected Output  Actual Output
#  15           15              15
#  10.35        10              10
#  'word'   value error     value error
