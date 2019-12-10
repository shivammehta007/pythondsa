"""
Dijkstra Quick Sort

Dijkstra Quick sort or Three way sort is another divide and conqure algorithm which has more
advantages than quick sort and is way faster if the element has a lot of duplicate keys. It creates
an invarianc similar to that of quicksort just it has two pointers one which says that left of
array is smaller and from one to second pointer all the elements are same and second to right
of it all bigger. So invariance looks something like this; 3, 2, 4, 1, 5, 5, 5, 5, 8, 10, 9.
Then this follows the furthur quick sort process.



Time Complexity: Divided by the number of permutations thus: log ( N! / x1! x2!)
Therefore by Sterling's inequality
Best Case: O(n)  # Randomized Quick sort with 3 way partitioning
Average Case: O(nlogn)
Worse Case: O(n^2) # This the case when array is already sorted therefore
                     it is recommended to do a random shuffle before sort

Example Usage:
``
    >>> import Quick3
    >>> a = [4, 5, 2, 1]
    >>> Quick3.sort(a)
    >>> a
    [1, 2, 4, 5]
``
"""
import random

class Quick3:
    """
    Quick3 Sort Class

    Methods:
    sort: Sorts the element, has to be called by the user
    """

    @staticmethod
    def sort(arr, uniform_shuffle=True):
        """
        Called by the user and invokes the whole quick sort ecosystem
        input:
        arr -> List of Numbers
        uniform_shuffle -> Boolean, True Invokes uniform shuffle
        """
        if uniform_shuffle:
            size = len(arr)
            for i in range(size-1):
                j = random.randint(i, size-1)
                arr[i], arr[j] = arr[j], arr[i]

        Quick3._quick3_sort(arr, 0, len(arr)-1)

    @staticmethod
    def _quick3_sort(arr, low, high):
        """
        Takes input array its lower pointer and higher pointer and recursively calls iteself
        until the array is sorted
        input:
        arr -> List of Numbers
        low -> integer starting pointer of this list
        high -> integer ending pointer of this list
        """
        if low < high:
            lesser_p, greater_p = Quick3._partition(arr, low, high)

            Quick3._quick3_sort(arr, low, lesser_p - 1)
            Quick3._quick3_sort(arr, greater_p + 1, high)

    @staticmethod
    def _partition(arr, low, high):
        """
        Partitions the subarray into three parts, first part has elements less than pivot
        element, second part has elements equal to the pivot and third has elements greater
        than the pivot element
        arr -> List of Numbers
        low -> current integer starting pointer of list
        high -> current integer ending pointer of list
        """
        lesser_p = low
        greater_p = high
        pivot = arr[low]
        i = low
        while i <= greater_p:
            if arr[i] < pivot:
                arr[lesser_p], arr[i] = arr[i], arr[lesser_p]
                lesser_p += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[greater_p] = arr[greater_p], arr[i]
                greater_p -= 1
            else:
                i += 1

        return lesser_p, greater_p

if __name__ == '__main__':
    from random import randint
    for _ in range(5):
        a = b = [randint(1, 100) for i in range(100)]
        Quick3.sort(a)
        assert a == sorted(b)
    print('Tests Passed Successfully')
