import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

# Use absolute import
from calc_operations import lst_operations as ls

# Rest of your code

# Print Log function
print(ls.get_log_function([1, 3, 4, 5]), "\n")