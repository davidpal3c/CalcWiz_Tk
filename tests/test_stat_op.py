import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)


from calc_operations import stat_op

print(stat_op.get_median([24, 35, 23, 21.4, 41,25.1]))