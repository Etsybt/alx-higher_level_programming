#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    sum_weight = 0
    total = 0

    for score, weight in my_list:
        sum_weight += score * weight
        total += weight
    
    if total == 0:
        return 0.0

    return sum_weight / total
