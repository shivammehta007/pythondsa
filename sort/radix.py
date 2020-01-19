"""
Radix Sort

It is an algorithm which is used to sort Integers in a faster manner.
It starts with the the least significant digit of an Integer and
puts it into the bucket according to it then pops the elements from
the bottom one by one and then it moves on to the next significant
digit and keeps on doing it until the most significant digit is
reached
Warning: Works only for Positive Integers
Time Complexity:
Average: O(Nd + k)
Space Complexity: O(N + k)
in this implementation k is 10 digits 0-9
and d is the number of max digits
"""
from collections import deque


class Radix:
    """
    This implementation of Radix sort uses buckets to keep the
    elements and then put it back onto the array
    """

    @staticmethod
    def sort(arr) -> list:
        """
        Calls the main sort function returns a list
        :param: arr -> list
        :return: arr -> list
        """
        RADIX = 10
        BUCKETS = [deque() for i in range(RADIX)]
        digit = 1

        max_number = max(arr)

        while digit <= max_number:

            for i in arr:
                current_digit = (i // digit) % RADIX
                BUCKETS[current_digit].append(i)

            i = 0

            for bucket in BUCKETS:
                while bucket:
                    arr[i] = bucket.popleft()
                    i += 1

            digit *= RADIX

        return arr


if __name__ == '__main__':
    from random import randint
    for _ in range(5):

        a = b = [randint(1, randint(1, 100000)) for i in range(100)]
        assert Radix.sort(a) == sorted(b)
    print('Tests Passed Successfully')
