#!/usr/bin/env python3
"""
Implementation of Binary Search

Binary Search is an algorithm which works on sorted arrays, by checking weather
the middle element is lesser or greater than the searching element
   Complexity:

   Best Case: O(1)
   Average Case: O(log n)
   Worst Case: O(log n)


It can be implemented in two ways recursively and without recursively

Typical Usage Examples:

>>> from pythondsa.search import Binary
>>> binary = Binary(recursion=True)
>>> array = [1, 2, 3, 4, 5, 6, 7]
>>> element = 2
>>> index = binary.search(array, element)
>>> index
1
>>> element = 9
>>> index = binary.search(array, element)
>>> index
-1

Input Parameters:
    recursion: True or False to use recursion or not

Methods:
    search: array -> input array type list
    element: # element to be searched for

"""


class Binary:
    """
    Implemenation of Binary Search

    Input of the seach should always be a sorted array, with element

    Attributed:
        recursion: A boolean indication of recusive method or not

    """
    def __init__(self, recursion=False):
        """
        Sets the searching algorithm by recursion parameter
        """
        self.recursion = recursion
        self.search = self.with_recursion if recursion \
            else self.without_recursion

    def without_recursion(self, array, element):
        """
        Binary Search without recursion

        Uses a linear approach instead of recusrion

        Parameters:
            array: list
            element: element to be searched

        Returns:
            -1: if element not found
            int: index of element in arrays
        """
        start_pointer = 0
        end_pointer = len(array) - 1
        index = -1
        while start_pointer <= end_pointer:
            mid = start_pointer + (end_pointer - start_pointer) // 2
            if array[mid] > element:
                end_pointer = mid - 1
            elif array[mid] < element:
                start_pointer = mid + 1
            else:
                return mid

        return index

    def with_recursion(self, array, element, start_pointer=-1, end_pointer=-1):
        """
        Binary Search with recursion

        Uses a recursive approach to search the array
        Parameters:
            array: list
            element: element to be searched
            start_pointer: used to point the starting location in recursion
            end_pointer: used to point the end location in recursion

        Returns:
            -1: if element not found
            int: index of element in arrays
        """
        if start_pointer == end_pointer == -1:
            start_pointer = 0
            end_pointer = len(array) - 1

        if start_pointer > end_pointer:
            return -1

        mid = start_pointer + (end_pointer - start_pointer) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            return self.with_recursion(array, element, start_pointer, mid-1)
        else:
            return self.with_recursion(array, element, mid+1, end_pointer)


if __name__ == '__main__':
    BS = Binary(recursion=True)
    ELEMENT = [0, 1, 2, 3, 4, 5, 6]
    X = [9, 4, 3, 10]
    RESULTS = [-1, 4, 3, -1]

    for i, x in enumerate(X):
        assert BS.search(ELEMENT, x) == RESULTS[i]
    print("Tests Sucessfull")
