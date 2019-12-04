#!/bin/usr/env python3
"""
Insertion Sort

For every iteration i it swap the a[i] with each large entity on its left

Complexity:
    Best Case: Sigma(n)
    Average Case: Theta(n^2)
    Worst Case: O(n^2)

When the array will be ordered, the insertion sort will just revalidate it with only one iteration.
Worst case: if array is descending order it makes 1/2 N^2 compares and 1/2 N^2 exchanges
Average Case: For partially sorted array with inversions less than < cN, it runsi n linear time the number of exchanges are equal to number of inversions.
"""

class Insertion:
    """
    Class to implement Insertion Sort
    """

    @staticmethod
    def sort(array):
        """
        Sort the array with insertion sort

        Parameters: array: python list
        Returns: sorted array : python list
        """
        N = len(array)
        for i in range(N):
            for j in range(i, 0, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]

        return array


if __name__ == '__main__':
    from random import randint
    for _ in range(5):
        a = b = [randint(1, 100) for i in range(100)]
        assert Insertion.sort(a) == sorted(b)
    print('Tests Passed Successfully')
