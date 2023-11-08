#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    t_weight = sum(weight for score, weight in my_list)
    w_sum = sum(score * weight for score, weight in my_list)
    return w_sum / t_weight
