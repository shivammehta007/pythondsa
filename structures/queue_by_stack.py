#!/usr/bin/env python3
"""
Implementation of Queues with the help of stacks

So the idea is to use two stacks one for enque i.e append
and the other is for deque i.e to pop
We always push into the first one and pop from second one
and if second stack is empty we first pop all from first
and transfer to second then pop from second

Example Usage:
``
    >>> q = Queue()
    >>> q.enque(1)
    >>> q.enque(2)
    >>> q.enque(3)
    >>> q.deque()
    1
    >>> q.deque()
    2
    >>> q.deque()
    3
    >>> len(q)
    0
    >>> q.deque()
    'Error'
``

Complexity:
Insertion : O(1)
Poping : O(1) aromatized*

"""


class Queue:
    """
    Implementation of queue class by stacks
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def __len__(self):
        return len(self.stack_1) + len(self.stack_2)

    def enqueue(self, inp):
        """
        Method used to add element to queue
        Parameters :
            inp: integer
        """
        self.stack_1.append(inp)

    def deque(self):
        """
        Method to remove element from the queue

        Returns:
           integer
           'Error' -> when queue is empty
        """
        if not self.stack_1 and not self.stack_2:
            return 'Error'

        while self.stack_1:
            self.stack_2.append(self.stack_1[len(self.stack_1)-1])
            del self.stack_1[len(self.stack_1)-1]

        output = self.stack_2[len(self.stack_2)-1]
        del self.stack_2[len(self.stack_2)-1]

        return output


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    assert q.deque() == 4
    assert q.deque() == 5
    assert q.deque() == 6
    assert q.deque() == 'Error'
    print('Test Passed Successfully')
