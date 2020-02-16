# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:50:43 2020

@author: Sergey
"""

#create a function for searching the lowest value in the array

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    

#create a function for selection sort
    
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

