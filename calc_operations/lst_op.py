from functools import reduce
import math

# 1.	Sorting
def get_sorted(lst):
    sorted_list = sorted(lst) 

    return sorted_list


# 2.	Finding Index
def get_index(lst, value):
    index = lst.index(value)
    if index == -1:
        return ValueError("Value not found in the list")
    else:
        return index


# 3.	Slicing
def get_slice(lst, slice_params):
    subset = lst[slice_params[0]: slice_params[1]]
    return subset 

# A Slice is a way to extract a portion of a sequence
# (list, tuple, or string) through a slice parameter 
# (a list containing two elements for start and stop positions) and returns the sliced list.


# 4.	Filtering

def get_filtered_val(input_list, condition):
    return list(filter(condition, input_list))

"""
def get_filtered_val(lst):
    filtered_values = [i for i in lst if i > 9]
    return filtered_values
"""

# 5.	Checking for Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]     # list slicing technique to produce 
                                #  a reversed copy of input list
#  if the list reads the same forwards as backward.

# =================================



def get_multiplied_values(lst, lst2):
    if len(lst) != len(lst2):
        raise ValueError("Lists must have the same length for element-wise multiplication")

    multiplied_vaues = [i * j for i, j in zip(lst, lst2)]
    return multiplied_vaues

def is_palindrome(lst):
    return lst == lst[::-1]













    