import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

# Use absolute import
from calc_operations import ht_op
from calc_operations import stat_op

fruit_quantity = {"Mango": 2.4,   
               "Strawyberry": 4,     
               "Avocado": 3,         
               "Blueberry":1.7}


fruit_color = {"Mango": "f2c84b",   
               "Strawyberry": "f2593a",     
               "Avocado": "b3c752",         
               "Blueberry":"2d56a8"}

print(ht_op.get_keys(fruit_quantity))
print(ht_op.get_max(fruit_quantity))
print(ht_op.has_key(fruit_quantity, "Avocado")) # returns boolean

print(stat_op.get_mean_ht(fruit_quantity))
