"""
Priority Queue

Priority Queues are used in certain cases where only top m elements has to be
kept in a certain order and minimum or maximum has to be popped at an optimum
time. Some use cases are like if we have to keep track of only 5 maximum tra-
nsaction in those scenarios Priority Queues can be used

There are two cases:

Ordered PriorityQueues:
Insert: O(NlogN)
Delete: O(1)

Unordered PriorityQueues:
Insert: O(1)
Delete: O(NlogN)

These can be implemented as MaxPriorityQueues or MinPriorityQueues

The Default will be Ordered MinPriorityQueue

Examples:
    ``
    >>> min_pq = PriorityQueues()
    >>> min_pq.insert(1)
    >>> min_pq.insert(5)
    >>> min_pq.insert(7)
    >>> min_pq.insert(4)
    >>> print(min_pq.q)
    [7, 5, 4, 1]
    >>> print(f'Min: {min_pq.findtop()}')
    Min: 1
    >>> print(f'Delete Min: {min_pq.delete()}')
    Delete Min: 1
    >>> print(f'Delete Min: {min_pq.delete()}')
    Delete Min: 4
    >>> print(min_pq.q)
    [7, 5]
    ``
"""

class PriorityQueues:
    """
    Priority Queues

    Parameters:
    ordered: Boolean -> Specified ordered or unordered priority queues
    max_heap: Boolean -> Specified Max and Min PriorityQueue
    capacity: Integer -> Put a limit to count of element
    """
    def __init__(self, ordered=True, max_heap=False, capacity=None):
        """
        Qrdered and MinPriorityQueue by default
        """
        self._ordered = ordered
        self._max = max_heap
        self._capacity = capacity
        self._N = 0
        self.q = []

    def insert(self, x):
        """
        Inserts the element into the PriorityQueues
        If the capacity is full it will automatically pop
        the elmenet at the max or min. Depending on the
        type of PriorityQueues
        """

        self.q.append(x)
        self._N += 1
        if self._capacity:
            if self._N - 1 == self._capacity:
                self.delete()

        if self._ordered:
            self.q.sort(reverse=(not self._max))

    def delete(self):
        """
        Deletes the maximum or minimum element from the queue, if the
        priority queue is ordered we can just pop otherwise we will
        have to sort and then pop
        """
        try:
            if self._N == 0:
                raise ValueError('Queue is already empty cannot delete')
            self._N -= 1
            if self._ordered:
                return self.q.pop()
            self.q.sort(reverse=(not self._max))
            return self.q.pop()

        except ValueError as err:
            print(err)
            return []

    def findtop(self):
        """
        Finds the Maximum or Minimum of the PriorityQueue
        Does not pops the element
        """
        try:
            if self._N == 0:
                raise ValueError('Queue is empty cannot find top element')
            self._N -= 1
            if self._ordered:
                return self.q[-1]
            self.q.sort(reverse=(not self._max))
            return self.q[-1]

        except ValueError as err:
            print(err)
            return []

if __name__ == '__main__':
    print('Min Queue')
    min_pq = PriorityQueues()
    min_pq.insert(1)
    min_pq.insert(5)
    min_pq.insert(7)
    min_pq.insert(4)
    print(min_pq.q)
    print(f'Min: {min_pq.findtop()}')
    print(f'Delete Min: {min_pq.delete()}')
    print(f'Delete Min: {min_pq.delete()}')
    print(min_pq.q)
    print('Max Queue')
    max_pq = PriorityQueues(max_heap=True, ordered=False, capacity=4)
    max_pq.insert(10)
    max_pq.insert(1)
    max_pq.insert(3)
    max_pq.insert(7)
    max_pq.insert(9)
    print(max_pq.q)
    print(f'Delete Max: {max_pq.delete()}')
    print(f'Delete Max: {max_pq.delete()}')
    print(f'Max: {max_pq.findtop()}')
    print(max_pq.q)
