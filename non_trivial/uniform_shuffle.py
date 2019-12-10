#!/usr/bin/env python3
"""
Uniform Shuffle

Shuffles the numbers in a uniform way, almost guarenteeing that the shuffle
will be random.
For every iteration it generates random number from 0 to index-1 and swaps the
current element from it.

Example Usage:
``
    >>>UniformShuffle.shuffle(ARRAY)
    [5, 3, 4, 0, 1, 2]
``
"""
import random


class UniformShuffle:
    """
    Class to uniform shuffle array
    """

    @staticmethod
    def shuffle(array, seed=None):
        """
        Shuffles the input array and returns input array
        Input: array -> list
        Output: array -> list
        """
        random.seed(seed)
        for i, value in enumerate(array):
            random_index = random.randint(0, max(0, i-1))
            temp = array[i]
            array[i] = array[random_index]
            array[random_index] = temp

        return array


if __name__ == '__main__':
    ARRAY = [0, 1, 2, 3, 4, 5]
    assert UniformShuffle.shuffle(ARRAY, 123) == [5, 3, 4, 0, 1, 2]
    assert UniformShuffle.shuffle(ARRAY, 25) == [2, 0, 3, 1, 5, 4]
    print('Tests passed successfully')
