#/usr/bin/env python3
"""
Implementation of Linear Search

Linear Search is an algorithm that checks for element one by one
until found linearly, hence the name Linear Search

    Complexity:
    Best Case: O(1)
    Average Case: O(n)
    Worst Case: O(n)

Methods:
    seach: array --> input array type list
           element --> elements to be searched for


Example Usage:
``
    >>> from pythondsa.search import Linear
    >>> linear = Linear()
    >>> array = [1,2,3,4,5]
    >>> element = 2
    >>> index = Linear.search(array, element)
    >>> index
    1
    >>> element = 7
    >>> index = Linear.search(array, element)
    >>> index
    -1
``
"""


class Linear:
    """
    Implementation of Linear Search
    """
    @staticmethod
    def search(array, element):
        """
        Linear Search

        Parameters:
            array: list
            element: element to find
        """
        for index, value in enumerate(array):
            if value == element:
                return index

        return -1


if __name__ == '__main__':
    LS = Linear()
    ELEMENT = [0, 1, 2, 3, 4, 5, 6]
    X = [9, 4, 3, 10]
    RESULTS = [-1, 4, 3, -1]

    for i, x in enumerate(X):
        assert LS.search(ELEMENT, x) == RESULTS[i]
    print("Tests Sucessfull")
