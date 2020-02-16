# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:45:49 2020

@author: Sergey Kubarev
"""

#basic algorythm for the binary search

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess < item:
            low = mid + 1
        if guess > item:
            high = mid - 1
        if guess == item:
            return mid
