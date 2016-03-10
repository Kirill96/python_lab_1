"""Storage of unique elements"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

def save_storage(store_set):
    """Save storage to the file"""
    with open('storage.txt', 'w') as file_save:
        for elem in store_set:
            file_save.write(elem + " ")


def load_storage():
    """Load storage from the file"""
    element = ""
    with open('storage.txt', 'r') as file_load:
        for line in file_load:
            element += line + " "

    return element


def storage():
    """Add, remove, find, list element in storage"""
    store = set()
    while True:
        menu = raw_input("\nInput command: ")
        menu_list = menu.split()
        if menu_list[0] == "add":
            for elem in menu_list[1:]:
                store.add(elem)
        elif menu_list[0] == "remove":
            for elem in menu_list[1:]:
                store.remove(elem)
        elif menu_list[0] == "find":
            elements = [el for el in menu_list[1:] if el in store]
            print elements
        elif menu_list[0] == "list":
            print [elem for elem in store]
        elif menu_list[0] == "save":
            save_storage(store)
        elif menu_list[0] == "load":
            for elem in load_storage().replace("\n", " ").split():
                store.add(elem)
        elif menu_list[0] == "grep":
            template = re.compile(menu[5:])
            print template.findall(str(store))
        elif menu_list[0] == "exit":
            return "End"
