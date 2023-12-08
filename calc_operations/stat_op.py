import statistics

# Statistical Operations:

#    Mean
def get_mean_lst(lst):
    # Check if hash table is not empty to avoid division by zero
    if len(lst) == 0:
        return None # choose to handle empty list some other way later
    mean = sum(lst) / len(lst)
    return mean


def get_mean_ht(ht):
    mean = sum(ht.values()) / len(ht)
    return mean

#    Median
def get_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n//2 -1] + sorted_lst[n//2]) / 2

    return median

"""
#    Standard Deviation
def get_std_dev(lst):
    std_dev = statistics.stdev(lst.values())
    return std_dev

"""