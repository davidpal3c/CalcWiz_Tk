import math

# 1. Power of each element
def get_power_item(lst):
    result = []
    for i in lst:
        if isinstance(i, str):
            print("Common, give me a break!")
        else:
            result.append(i**2)        
    return result



# 2. Absolute Values
def get_absolute_val(lst):
    absolute_value = [abs(i) for i in lst]
    return absolute_value

# The absolute value function, often denoted as ∣x∣, is a mathematical
# function that returns the distance of a number from zero on the 
# number line, regardless of its direction. In other words, it gives the
# magnitude or size of a real number without considering its sign.
# Used in sorting/ranking/calculating distances/comparing magnitudes
# /error metrics/error handling calculations/handling user input/ solving equations/etc.

# The abs() function or the idea of absolute value is a tool that 
# can be useful in handling specific scenarios where the sign of 
# a value is not relevant to the desired outcome.


# 3. Square Root
def get_square_root1(lst):
    sqrt_values = [math.sqrt(i) if i >= 0 else f"Cannot calculate square root of {i} since it is a negative value" for i in lst]  
    return sqrt_values

def get_square_root(lst):               #function gives square roots of items including negative values by taking them as absolute values
    sqrt_values = [math.sqrt(abs(i)) for i in lst]
    return sqrt_values


# 4. Rounding
def get_rounded_value(lst):
    rounded_values = [round(i, 1) for i in lst]
    return rounded_values




# Addition
# Substraction
# Multiplication
# Division ('/'):
# Exponentiation ('**'):
# Modulus ('%'):

# Logical AND ('and'):
# Logical OR ('or'):
# Logical XOR (Exclusive OR):

# Equality ('=='):

# Inequality ('!='):

"""These operations can be applied to other iterable data structures like NumPy 
arrays or Pandas DataFrames in Python. The specific operations you choose 
depend on the type of data and the problem you are trying to solve"""

