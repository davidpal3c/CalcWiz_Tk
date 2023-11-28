from functools import reduce
import math

def get_sum(lst):
    sum_total = sum(lst)

    return sum_total



def get_average(lst):
    return sum(lst) / len(lst)


def get_max(lst):
    max_val = float("-inf")      
                # Initializes mx to negative infinity. This ensures that any 
                # element in the list will be greater than this initial value.
    for num in lst:
        if num > max_val:
            max_val = num
    
    return mx

    # If mn = float("inf"), Initializes mn to positive infinity. This ensures 
    # that any element in the list will be lower than this initial value.
    # Both functions could initialize a variable to either negative infinity 
    # (get_max) or positive infinity (get_min) and then iterate through the input list,
    #  updating the variable whenever they find a new maximum or minimum value, respectively. 
    # The result is the maximum or minimum value in the list, depending on the function.

def get_min(lst):
    min_val = min(lst)

    return min_val



def get_sorted(lst):
    sorted_list = sorted(lst) 

    return sorted_list


def get_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 ==1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n//2 -1] + sorted_lst[n//2]) / 2

    return median


"""def get_median2(lst):
    lst = sorted(lst)

    if len(lst) % 2 == 0:
        return (lst[(len(lst)//2) -1] + lst[(len(lst) // 2 )]) / 2
    else:
        return lst[(len(lst)-1)/2]
"""

def get_product(lst):
    product = reduce(lambda x, y : x * y, lst)

    return product


# The reduce function is part of the functools module in Python.
# It is designed to perform a cumulative operation on the items of
#  an iterable (e.g., a list) and reduce it to a single accumulated
#  result. The syntax of the reduce regular-function is as follows:

"""
# Define a regular function for multiplication
def multiply(x, y):
    return x * y

# Example list
my_list = [1, 2, 3, 4, 5]

# Use reduce with the multiply function
product = reduce(multiply, my_list)

print(product)
"""

            # count method is a method used to count the 
            # occurrences of a particular element within the list.
            # (as opposed to count, len provides the lenght of a sequence,
            #  regardless of the specific values it contains) 
def get_count(lst):

    return lst.count(3)

# Be aware that using count on an item not present in the list
# will return 0, whereas trying to find the length of a non-existent list
#  (or other non-iterable) will result in an error.


def get_index(lst):
    index = lst.index("banana")
    return index


def get_slice(lst):
    subset = lst[4:-1]
    return subset 

# A Slice is a way to extract a portion of a sequence
# (list, tuple, or string)

def get_power_item(lst):
    result = []
    for i in lst:
        if isinstance(i, str):
            print("Common, give me a break!")
        else:
            result.append(i**2)        
    return result


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

def get_square_root1(lst):
    sqrt_values = [math.sqrt(i) if i >= 0 else f"Cannot calculate square root of {i} since it is a negative value" for i in lst]  
    return sqrt_values

def get_square_root(lst):               #function gives square roots of items including negative values by taking them as absolute values
    sqrt_values = [math.sqrt(abs(i)) for i in lst]
    return sqrt_values

def get_rounded_value(lst):
    rounded_values = [round(i, 1) for i in lst]
    return rounded_values

def get_cumulative_sum(lst):
    cumulative_sum = [sum(lst[:i+1]) for i in range(len(lst))]
    return cumulative_sum

# A cumulative sum is computed by adding up the elements of the list progressively.
# Each element in the cumulative sum list is the sum of all the preceding 
# elements in the original list up to that point.
# It is commonly used in Financial or Stock Market Analysis/Budgeting, Signal Processing, 
# Project Management (tracking resource usage, or man-hours or costs), 
# Inventory Management, Quality control, Physics/Engineering (energy consumption, 
# cumulative displacement), Web Analytics (track user engagement metrics, etc),
# Population Studies (Demographic analysis, etc).  

def get_filtered_val(lst):
    filtered_values = [i for i in lst if i > 9]
    return filtered_values

def get_multiplied_values(lst, lst2):
    if len(lst) != len(lst2):
        raise ValueError("Lists must have the same length for element-wise multiplication")

    multiplied_vaues = [i * j for i, j in zip(lst, lst2)]
    return multiplied_vaues


# adding a constant
# See operations in depth for types and uses

def get_add_constant(lst):
    constant = 0
    result = [i * constant for i in lst]
    return result


def get_exponential_func(lst):
    exponential_values = [math.exp(i) for i in lst]
    return exponential_values


# (inverse of exponential function), if b to the power of y equal x, 
# then the log function is log'b'(x) = y 

def get_log_function(lst):
    log_values = [math.log10(i) for i in lst]        # (base 10 log function)
    return log_values


def get_sin_value(lst):
    angle = math.radians(lst)        #convert degrees to radians
    sin_value = math.sin(angle)
    return sin_value












    