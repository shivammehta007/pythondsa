"""
Counting Sort

It is an linear time sorting algorithm which can be used when the number of
unique elements in the array is small, as it takes arbitary space.
How it works is that It takes an array and just count number of occurancies
of all the elements and put it back in a sequential manner

Time Complexity: O(N + M)

Space Complexity: O(M)

Example Usage:
``
    >>> import Counting
    >>> a = [4, 5, 2, 1]
    >>> Counting.sort(a)
    [1, 2, 3, 4]
``
"""


class Counting:
    """
    Counting Sort Class

    Methods:
    sort: Sorts the list and returns the sorted value
    """

    @staticmethod
    def sort(arr) -> list:
        """
        This method is invoked and it sorts the array
        Input:
        :param: arr input array
        :return: list sorted list
        """
        max_value = max(arr)
        counting_array = [0 for _ in range(max_value + 1)]
        for v in arr:
            counting_array[v] += 1

        sorted_array = []
        for i, v in enumerate(counting_array):
            if v:
                while v:
                    v -= 1
                    sorted_array.append(i)

        return sorted_array


if __name__ == '__main__':
    assert Counting.sort([4, 5, 2, 1]) == [1, 2, 4, 5]
    assert Counting.sort([6, 7, 8, 9]) == [6, 7, 8, 9]
    assert Counting.sort([5, 2, 7, 1, 9, 9, 9, 2]) == [1, 2, 2, 5, 7, 9, 9, 9]
    print('Tests Passed')
