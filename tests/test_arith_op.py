import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

# Use absolute import
from calc_operations import arithmetic_op as arith_op

print(arith_op.get_average([4352,3242, 352.23, 7257, 1230, 2302]))
