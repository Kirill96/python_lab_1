"""Input numbers for sort"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def input_numbers():
    """array of numbers for sort"""
    array_numbers = raw_input("\nInput numbers: ").split()
    i = 0
    for elem in array_numbers:
        array_numbers[i] = int(elem)
        i += 1

    return array_numbers
