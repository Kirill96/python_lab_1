"""fibonacci generator"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def fibonacci(max_number):
    """Generator fibonacci"""
    fst_number, snd_number = 0, 1
    while fst_number < max_number:
        yield fst_number
        fst_number, snd_number = snd_number, fst_number + snd_number
        