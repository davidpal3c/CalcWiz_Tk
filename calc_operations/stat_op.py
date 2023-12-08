import statistics

# Statistical Operations:
#    Mean
def get_mean(lst):
    mean = sum(lst.values()) / len(lst)
    return mean


#    Median
def get_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 ==1:
        median = sorted_lst[n // 2]
    else:
        median = (sorted_lst[n//2 -1] + sorted_lst[n//2]) / 2

    return median

#    Standard Deviation

def get_std_dev(lst):
    std_dev = statistics.stdev(lst.values())
    return std_dev
