#/bin/usr/end python3
"""
Selection Sorting for dataset

Selection sort is not really used very often because of the overhead of running
time compleity, but the way it works is really very easy:
Steps:
1. for iterstion i look for the minimum element from i to N
2. swap the minimum value with the value at i i.e echange(a[i], min)

Complexity:
    Best : O(n^2)
    Average: O(n^2)
    Worst : O(n^2)

Even if array is sorted, the whole array is traversed hence again O(n^2)

"""


class Selection:
    """
    Class to implement selection
    """

    @staticmethod
    def sort(array):
        """
        Sort into selection sort

        Parameters: array : python list
        Returns: sorted array
        """
        N = len(array)
        for i in range(N):
            mini = i
            for j in range(i+1, N):
                if array[j] < array[mini]:
                    mini = j

            array[mini], array[i] = array[mini], array[i]
        return array


if __name__ == '__main__':
    ARRAY = [1, 6, 4, 2, 9, 0]
    print(Selection.sort(ARRAY))
