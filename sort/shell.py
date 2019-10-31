#!/usr/bin/env python3
"""
Shell Sorting Algorithm uses h-window size to skim through the array and sort
then it reduces the window size in some order and then again sort the array
with elements on its index unless it reaches 1 where it acts as an insertion
sort

"""


class Shell:

    def sort(self, array):
        N = len(array)
        h = 1
        while h < N/3:
            h = 3*h + 1
        print(N)
        while h >= 1:
            i = h
            while i < N:
                j = i
                while j >= h:
                    if array[j] > array[j-h]:
                        temp = array[j]
                        array[j-h] = array[j]
                        array[j] = temp
                    j -= h
                i += 1

            h //= 3
        return array


if __name__ == '__main__':
    arr = [2, 3, 4, 0, 1, 5]
    sorter = Shell()
    print(sorter.sort(arr))
