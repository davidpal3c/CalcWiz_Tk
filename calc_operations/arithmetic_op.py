from functools import reduce
import math

# Arithmetic Operations

# 1. Summation
def get_sum(lst):
    sum_total = sum(lst)

    return sum_total

# 2. Average
def get_average(lst):
    return sum(lst) / len(lst)

# 3. Maximum and Minimum
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


# 4. Product
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

# 5. Count
def get_count(lst):

    return lst.count(3)
 # count method is a method used to count the 
            # occurrences of a particular element within the list.
            # (as opposed to count, len provides the lenght of a sequence,
            #  regardless of the specific values it contains) 

# Be aware that using count on an item not present in the list
# will return 0, whereas trying to find the length of a non-existent list
#  (or other non-iterable) will result in an error.






# 6. Cumulative Sum
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


# 7. Adding a Constant
# See operations in depth for types and uses
def get_add_constant(lst):
    constant = 0
    result = [i * constant for i in lst]
    return result


# Element-wise Addition (+):
# result = [x + y for x, y in zip(list1, list2)]