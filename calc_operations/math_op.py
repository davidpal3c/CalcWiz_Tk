import math
from decimal import Decimal, getcontext

# Set the precision to a sufficiently large value
getcontext().prec=50

# Exponential Function
def get_exponential_func(lst):
    exponential_values = [Decimal(i).exp() for i in lst]
    return exponential_values


# (inverse of exponential function), if b to the
# power of y equal x, 
# then the log function is log'b'(x) = y 


# Logarithmic Function
def get_log_function(lst):
    log_values = [math.log10(i) for i in lst]        # (base 10 log function)
    return log_values

    # add the other log function (base)

# Trigonometric Functions
def get_sin_value(lst):
    angle = math.radians(lst)        #convert degrees to radians
    sin_value = math.sin(angle)
    return sin_value

