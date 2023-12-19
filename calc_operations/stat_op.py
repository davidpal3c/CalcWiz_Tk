import statistics
import numpy as np

# Statistical Operations:

#    Mean
def get_lst_mean(lst):
    # Check if list is not empty to avoid division by zero
    if len(lst) == 0:
        return None # choose to handle empty list some other way later
    mean = sum(lst) / len(lst)
    return mean


def get_ht_mean(ht):
    mean = sum(ht.values()) / len(ht)
    return mean

#    Median (lists)
def get_lst_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n//2 -1] + sorted_lst[n//2]) / 2

    return median

# Median (hash tables)
def get_ht_median(ht):
    values = list(ht.values())
    return get_lst_median(values)



#    Standard Deviation (sample)
def get_sample_std_dev_lst(lst):
    std_dev = statistics.stdev(lst)
    return std_dev

#    Standard Deviation (population)
def get_population_std_dev_lst(lst):
    std_dev = np.std(lst)
    return std_dev



