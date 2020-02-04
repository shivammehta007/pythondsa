"""
Heap Sort

Heap sorting is an unstable sorting algorithm but it is inplace, and works in best, worst
and average case of O(n logn). It uses max heap datastructure in the back.
The algorithm is pretty simple construct a max heap {O(n)} and keep on swapping the maximum
element with the last element of the unsorted array.

For the sake of learning we will implement sorting heap methods again, we coudl have used Heap
from structure.Heap

Time Complexity:
Best Case: O(nlogn)
Average Case: O(nlogn)
Worse Case: O(nlogn)

Example Usage:

```
    >>> import Heap
    >>> a = [5, 4, 7, 2, 1]
    >>> Heap.sort(a)
    >>> a
    [1, 2, 4, 5, 7]
```

"""

class Heap:
    """
    Heap Sort class

    Methods:
    sort: Sorts the elments, has to be called by the user
    """

    def _parent(self, node):
        """Return parent index of node"""
        return (node - 1) // 2

    def _has_left_child(self, node, arr):
        """Checks for left child of a node"""
        return 2*node + 1 < len(arr)

    def _has_right_child(self, node, arr):
        """Checks for right child of a node"""
        return 2*node + 2 < len(arr)

    def _right_child(self, node):
        """Returns right child of a node"""
        return 2*node + 2

    def _left_child(self, node):
        """Returns left child of a node"""
        return 2*node + 1

    def _swap(self, arr, i, j):
        """swap two indexes in array"""
        arr[i], arr[j] = arr[j], arr[i]

    def __init__(self, arr):
        self.heapify(arr)

    def downheap(self, node, arr, end=None):
        """
        Down Heap method to maintain Max Heap property when element node is
        a parent node
        """
        if self._has_left_child(node, arr):
            if not end or (end and self._left_child(node) < end):
                greater_child = self._left_child(node)

                if self._has_right_child(node, arr):
                    if not end or (end and self._right_child(node) < end):
                        greater_child = self._right_child(node) \
                            if arr[self._right_child(node)] > arr[greater_child] else greater_child

                if arr[greater_child] > arr[node]:
                    self._swap(arr, node, greater_child)
                    self.downheap(greater_child, arr, end)

    def heapify(self, arr):
        """Converts the array into max heap"""
        start = self._parent(len(arr) - 1)
        for i in range(start, -1, -1):
            self.downheap(i, arr)


    @staticmethod
    def sort(arr):
        """
        Sorts the Array by converting it into maxheap first and then swapping the maximum element
        into the last working position of the array
        """
        heap = Heap(arr)

        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heap.downheap(0, arr, i)


if __name__ == '__main__':
    from random import randint
    for _ in range(5):

        a = b = [randint(1, randint(1, 100000)) for i in range(100)]
        Heap.sort(a)
        assert a == sorted(b)
    print('Tests Passed Successfully')
