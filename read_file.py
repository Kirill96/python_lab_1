"""Read data from file"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def read_file(name_of_file):
    """Read data from file"""
    with open(name_of_file, 'r') as f_read:
        list_of_data = f_read.readlines()

    return list_of_data
