"""
Quick Sort

Quick sort is another of divide and conquer algorithms which recursively divides the array into
two subarrays but it is done after the work is done, unlike the merge sort where the recusrion takes
place first and then the work is done.
In quicksort we first start with an arbitary element and call it as the number which we need to find
its currect location, we start with the first position as i and last as j for that subarray and move
these pointers and swap them unless all the elements to the right of the intersection of pointers
are less than the comparision element and all the elements to the left of the intersection of
pointers are greater than the element. Then return the partition at this moment the element of that
partition is at its correct position.

Fun Fact: It is faster than mergesort even though it has 39% more comparisions because of less
          movement of data, as mergesort has to move data in and out of auxillary array

Time Complexity:
Best Case: O(nlogn) # case when it divides everything in half
Average Case: O(nlogn)
Worse Case: O(n^2) # This the case when array is already sorted therefore
                     it is recommended to do a random shuffle before sort

Example Usage:
``
    >>> import Quick
    >>> a = [4, 5, 2, 1]
    >>> Quick.sort(a)
    >>> a
    [1, 2, 4, 5]
``
"""
import random

class Quick:
    """
    Quick Sort Class

    Methods:
    sort: Sorts the element, has to be called by the user
    """

    @staticmethod
    def sort(arr, uniform_shuffle=True):
        """
        Called by the user and invokes the whole quick sort ecosystem
        input:
        arr -> List of Numbers
        uniform_shuffle -> Boolean, True invokes uniform shuffle
        """
        if uniform_shuffle:
            size = len(arr)
            for i in range(size-1):
                j = random.randint(i, size-1)
                arr[i], arr[j] = arr[j], arr[i]

        Quick._quick_sort(arr, 0, len(arr)-1)

    @staticmethod
    def _quick_sort(arr, low, high):
        """
        Takes input array its lower pointer and higher pointer and recursively calls iteself
        until the array is sorted
        input:
        arr -> List of Numbers
        low -> integer starting pointer of this list
        high -> integer ending pointer of this list
        """
        if low < high:
            _pi = Quick._partition(arr, low, high)

            Quick._quick_sort(arr, low, _pi-1)
            Quick._quick_sort(arr, _pi+1, high)

    @staticmethod
    def _partition(arr, low, high):
        """
        Partitions the subarray, keeps first element of low as the comparision element and finds
        its correct location into the array.
        input:
        arr -> List of Numbers
        low -> current integer starting pointer of list
        high -> current integer ending pointer of list
        """
        i = low + 1
        j = high
        while j >= i:
            while i <= high and arr[i] < arr[low]:
                i += 1
            while arr[j] > arr[low]:
                j -= 1
            if j >= i:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

if __name__ == '__main__':
    A = [23, 54, 76, 12, 11, 4, 90]
    Quick.sort(A)
    assert A == [4, 11, 12, 23, 54, 76, 90]
    print('Test Passed')
