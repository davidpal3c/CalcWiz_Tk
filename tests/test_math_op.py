import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)


from calc_operations import math_op

print(f"The Exponential Values of the provided list, are: \n {math_op.get_exponential_func([1, 2, 4])}")