#!/usr/bin/env python3
"""
Merge Sort

Merge sort uses Divide and Conquer technique to divie big problems into small
ones.We break the array into two parts and keep on breaking until it is single
element then we merge them based on their place in sorting
Usage: 

>>> Merge.sort([3,2,1,6,4,5])
[1,2,3,4,5,6]
"""


class Merge:
    """
    Class to implement merge sorting Technique
    """

    @staticmethod
    def _merge(left_array, right_array):
        print(left_array, right_array)
        merged_array = []
        l, r = 0, 0
        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                merged_array.append(left_array[l])
                l += 1
            else:
                merged_array.append(right_array[r])
                r += 1

        return merged_array

    @staticmethod
    def sort(array):
        N = len(array)

        if N >= 2:
            left_array = Merge.sort(array[:N//2])
            right_array = Merge.sort(array[N//2:])
            array = Merge._merge(left_array, right_array)

        return array


if __name__ == '__main__':
    print(Merge.sort([3, 2, 1, 5, 6, 4]))
