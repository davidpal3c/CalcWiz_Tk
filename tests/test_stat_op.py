import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)


from calc_operations import stat_op


dictionary_1 = {"CRT12960": 1200, 
                "CRT130100" : 2100, 
                "CRT140400": 1899, 
                "CRT160300": 2499,
                "CRS110400": 2699}

print(f"Mean: {stat_op.get_mean_lst([24, 35, 23, 21.4, 41,25.1])}")

print(f"Median: {stat_op.get_median_lst([30, 40, 50, 60])}")
print(f"Median (hash table): {stat_op.get_mean_ht(dictionary_1)}")

print(f"Standard Deviation (sample): {stat_op.get_sample_std_dev_lst([140, 230, 510, 728, 102])}")
print(f"Standard Deviation (population): {stat_op.get_population_std_dev_lst([140, 230, 510, 728, 102])}")
