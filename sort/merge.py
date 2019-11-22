#!/usr/bin/env python3
"""
Merge Sort

Merge sort uses Divide and Conquer technique to divie big problems into small
ones.We break the array into two parts and keep on breaking until it is single
element then we merge them based on their place in sorting.

Time Complexity:
Best: O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)

Usage:

>>> Merge.sort([3,2,1,6,4,5])
[1,2,3,4,5,6]
"""


class Merge:
    """
    Merge Sort Class

    Class to implement merge sorting Technique
    Methods:
    sort: Sorts the element, has to be called by the user
    """

    @staticmethod
    def _merge(left_array, right_array):
        """
        Merges the left array and right array in a sorted manner
        Input:
        left_array -> list
        right_array -> list

        Output:
        merged_array -> merged and sorted list
        """
        merged_array = []
        l, r = 0, 0
        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                merged_array.append(left_array[l])
                l += 1
            else:
                merged_array.append(right_array[r])
                r += 1

        if l < len(left_array):
            merged_array.extend(left_array[l:])
        if r < len(right_array):
            merged_array.extend(right_array[r:])

        return merged_array

    @staticmethod
    def sort(array):
        """
        Calls the sort operation recusrively until the size of array is 1
        Input:
        array -> List

        Output:
        array -> Sorted List
        """
        N = len(array)

        if N >= 2:
            left_array = Merge.sort(array[:N//2])
            right_array = Merge.sort(array[N//2:])
            array = Merge._merge(left_array, right_array)

        return array


if __name__ == '__main__':
    assert Merge.sort([3, 2, 1, 5, 6, 4]) == [1, 2, 3, 4, 5, 6]
    assert Merge.sort([56, 23, 89, 10, 45, 11]) == [10, 11, 23, 45, 56, 89]
    print('Tests ran successfully')
