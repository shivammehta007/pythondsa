#/usr/bin/env python3
"""
Implementation of stacks with the help of queues

Two Queues are used to depict a stack the whole overhead
is done while pushing the element, if queue1 is empty
simply push in queue2 otherwise switch all the entities
and then push to queue 2 and empty queue 1

Example Usage:
``
    >>> s = Stack()
    >>> s.push(5)
    >>> s.push(4)
    >>> s.pop()
    4
    >>> s.pop()
    5
    >>> s.pop()
    'Error'
``

Complexity:
    Push: O(N)
    Pop : O(1)
"""

class Stack:
    """
    Impelementation of stack with queues

    Two queues work together one by one to achieve stacks
    """

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def __len__(self):
        return len(self.queue_1) + len(self.queue_2)

    def push(self, inp):
        """
        Pushes the element into the stack
        Input:
           inp: array
        """
        if not self.queue_1 and not self.queue_2:
            self.queue_1.append(inp)

        elif self.queue_1:
            self.queue_2.extend(self.queue_1)
            self.queue_2.append(inp)
            self.queue_1 = []
        else:
            self.queue_1.extend(self.queue_2)
            self.queue_1.append(inp)
            self.queue_2 = []

    def pop(self):
        """
        Pops out the topmost element from the stack
        Returns:
             int
        """
        output = ''
        if not self.queue_1 and not self.queue_2:
            output = 'Error'
        elif self.queue_1:
            output = self.queue_1[len(self.queue_1)-1]
            del self.queue_1[len(self.queue_1)-1]
        else:
            output = self.queue_2[len(self.queue_2)-1]
            del self.queue_2[len(self.queue_2)-1]
        return output

if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push(5)
    s.push(6)
    assert s.pop() == 6
    assert s.pop() == 5
    assert s.pop() == 4
    assert s.pop() == 'Error'
    print("Test Passes Successfully")
