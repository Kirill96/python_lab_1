"""The first lab python2.7"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#import _input
#import input_numbers
import task1
import task2
import task3
import task4
import task5_re
import read_file
import argparse

__parser__ = argparse.ArgumentParser()
__parser__.add_argument('number_task')
__parser__.add_argument('file_name')
__command_str__ = __parser__.parse_args()

__list_of_data__ = read_file.read_file(__command_str__.file_name)
#__menu__ = int(raw_input("\n1. Task_1; \n2. Task_2; \
#			             \n3. Task_3; \n4. Task_4. \n Your choice: "))
if __command_str__.number_task == "1":
    print task1.item1(__list_of_data__[1])
    print task1.item2(__list_of_data__[2])
    print task1.item3(__list_of_data__[3])
    print task1.item4(__list_of_data__[4])
elif __command_str__.number_task == "2":
    __list_numbers__ = []
    for element in __list_of_data__[6].split():
        __list_numbers__.append(int(element))
    print "Quick sort: ", task2.quick_sort(__list_numbers__)
    print "Merge sort: ", task2.merge_sort(__list_numbers__)
    print "Radix sort: ", task2.radix_sort(__list_numbers__)
elif __command_str__.number_task == "3":
    print task3.storage()
elif __command_str__.number_task == "4":
    __max_number_for_fib__ = int(__list_of_data__[8])
    for number in task4.fibonacci(__max_number_for_fib__):
        print number,
elif __command_str__.number_task == "5":
    print "Email: ", task5_re.valid_email()
    print "Number: ", task5_re.valid_number()
    print "\nURL:\n", task5_re.url()
else:
    print "Error!"
