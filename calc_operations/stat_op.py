# Statistical Operations:

#    Mean

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

