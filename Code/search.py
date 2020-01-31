#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    # Time complexity: O(n)
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # Time complexity: O(n)
    if array[index] == item:
        return index
    elif index == len(array) - 1:
        return None
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Time complexity: O(log(2)n)
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_item = array[mid]
        
        if mid_item < item:
            left= mid + 1
        
        elif mid_item == item:
            return mid
        
        elif mid_item < item:
            left= mid + 1
        
        else:
            right = mid - 1
    
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # Time complexity: O(log(2)n)
    if left > right:
        return None
    
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    mid = (right + left) // 2
    
    if array[mid] == item:
        return mid
    
    elif array[mid] > item:
        return binary_search_recursive(array, item, left, mid - 1)
    
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid + 1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    # return binary_search_recursive()
