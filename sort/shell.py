#!/usr/bin/env python3
"""
Shell Sorting Algorithm uses h-window size to skim through the array and sort
then it reduces the window size in some order and then again sort the array
with elements on its index unless it reaches 1 where it acts as an insertion
sort.
Time Complexity:
    Best: O(n log n)
    Average: O(n (log n)^2 )
    Worst: O (n (log n)^2 )
    No One can calculate it since for every different array it takes different
    number of comparisons to do it but it looks like its O(n^{3/2}) but it is
    not it is relatively way much faster somewhere between O(nlog_3n).
    Since its very light and fast it is used in various embedding systems

Example Usage:
``
    >>>Shell.sort([3, 2, 1, 4])
    [1, 2, 3, 4]
``
"""


class Shell:
    """
    Shell Sort class implementation use sort method to sort and return array
    """
    @staticmethod
    def sort(array):
        """
        Sorts the input unsorted array and returns the sorted array
        Input: array -> list of integers
        Output: array -> list of sorted integers
        """
        N = len(array)
        h = 1
        # Populate the h-size
        while h < N//3:
            h = 3*h + 1

        while h >= 1:
            i = h
            while i < N:
                j = i
                while j >= h:
                    if array[j] < array[j-h]:
                        temp = array[j]
                        array[j] = array[j-h]
                        array[j-h] = temp
                    j -= h
                i += 1

            h //= 3
        return array


if __name__ == '__main__':
    from random import randint
    for _ in range(5):
        a = b = [randint(1, 100) for i in range(100)]
        assert Shell.sort(a) == sorted(b)
    print('Tests Passed Successfully')
