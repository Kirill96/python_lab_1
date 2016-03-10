"""Sort"""
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def quick_sort(array_numbers):
    """sorting numbers by quicksort"""
    less = []
    pivot_list = []
    more = []
    if len(array_numbers) <= 1:
        return array_numbers
    else:
        pivot = array_numbers[0]
        for i in array_numbers:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more


def merge_sort(array_numbers):
    """sorting numbers by merge sort"""
    if len(array_numbers) <= 1:
        return array_numbers

    middle = len(array_numbers) // 2
    left = array_numbers[:middle]
    right = array_numbers[middle:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """sorting left and right part of array in result array"""
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left:
        result.extend(left[left_index:])
    if right:
        result.extend(right[right_index:])

    return result


def radix_sort(array_numbers):
    """sort array of numbers by radix sort"""
    length = len(str(max(array_numbers)))
    rang = 10
    for i in range(length):
        prime = [[] for k in range(rang)]
        for elem in array_numbers:
            figure = elem // 10**i % 10
            prime[figure].append(elem)
        array_numbers = []
        for k in range(rang):
            array_numbers = array_numbers + prime[k]

    return array_numbers
