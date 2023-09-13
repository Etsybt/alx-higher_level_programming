#!/usr/bin/python3
def uniq_add(my_list=[]):
    integer_set = set()
    outcome = 0

    for number in my_list:
        if number not in integer_set:
            outcome += number
            integer_set.add(number)

    return outcome
