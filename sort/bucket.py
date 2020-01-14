"""
Bucket Sort

Bucket sort transfers all the elments into buckets of equal interval and then
do a insertion sort in those buckets itself and then iterates them to get a
sorted array

Complexity:
Time: O(N+M)
Space: O(N+M)
"""
from insertion import Insertion


class Bucket:
    """
    Bucket Sort to sort for Integer numbers use sort method to return sorted
    array
    """

    @staticmethod
    def sort(array):
        """
        Sorts the input unsorted array and returns the sorted array
        :param: array -> list of integers
        :returns: array -> list of sorted integers
        """

        max_element = max(array)
        length = len(array)
        bucket_size = max_element/length

        buckets = [[] for _ in range(length)]

        for i in range(length):
            bucket_number = int(array[i] // bucket_size)

            if bucket_number != length:
                buckets[bucket_number].append(array[i])
            else:
                buckets[bucket_number - 1].append(array[i])

        for i in range(length):
            buckets[i] = Insertion.sort(buckets[i])

        sorted_array = []
        for i in range(length):
            sorted_array.extend(buckets[i])

        return sorted_array


if __name__ == '__main__':
    from random import randint
    for _ in range(5):
        a = b = [randint(1, 100) for i in range(100)]
        assert Bucket.sort(a) == sorted(b)
    print('Tests Passed Successfully')
