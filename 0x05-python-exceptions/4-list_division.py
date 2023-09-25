#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    outcome = []
    for n in range(list_length):
        try:
            outcome.append(my_list_1[n] / my_list_2[n])
        except ZeroDivisionError:
            print("division by 0")
            outcome.append(0)
        except TypeError:
            print("wrong type")
            outcome.append(0)
        except IndexError:
            print("out of range")
            outcome.append(0)
        finally:
            pass
    return outcome
