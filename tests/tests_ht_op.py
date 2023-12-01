import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from calc_operations import ht_operations as ht 

h = {"Simon":23, "Elsa":28, "Tim":34, "Michelle":29}


print(ht.get_keys(h))
