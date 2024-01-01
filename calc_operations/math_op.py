import math
from decimal import Decimal, getcontext

# Set the precision to a sufficiently large value
getcontext().prec=80

# Exponential Function
def get_exponential_func(lst):
    exponential_values = []
    
    for i in lst:
        try:
            exp_value = Decimal(str(i)).exp()
            rounded_value = round(float(exp_value), 3)
            exponential_values.append(rounded_value)
        except decimal.InvalidOperation:
            exponential_values.append(None)  # or handle as needed

    return exponential_values


# (inverse of exponential function), if b to the
# power of y equal x, 
# then the log function is log'b'(x) = y 


# Logarithmic Function


    # add the other log function (base)

# Trigonometric Functions
def get_sin_value(lst):
    sin_values = [math.sin(math.radians(angle)) for angle in lst]
    return sin_values


# Sin value for single unit
"""
def get_sin_value(lst):
    angle = math.radians(lst)        #convert degrees to radians
    sin_value = math.sin(angle)
    return sin_value
"""
