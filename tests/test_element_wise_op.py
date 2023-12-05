import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)


from calc_operations import element_wise_op as element_wOperation

# testing module function
print(element_wOperation.get_square_root([64, 16, 32, 144]))
