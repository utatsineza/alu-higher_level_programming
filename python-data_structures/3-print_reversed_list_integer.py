#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ''
    else:
        my_list.reverse()
        length = len(my_list)
        for i in range(length):
            print("{:d}".format(my_list[i]))
