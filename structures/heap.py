"""
Heap

Heap is the kind of datastructure where a heap order property is maintained
that is in Heap T for every element position p the value of p should be 
greater than the parent of p.
In a complete binary heap a complete binary tree property is maintained and
the height of the tree is log n.
We will implement a min heap, a max heap is just the direct opposite of it.

Insertion in a Heap: an element is added on the base or the last position
then up-heap bubbling is performed that is the element is swapped with its
root until the root is smaller than it and its leaves are greater than it.
Time Complexity: Wose case: O(log n) Average Case: O(1)

Deletion in a Heap, the removal of minimum occurs in a way that we swap the
first element with the last element and pop the value from the heap.
Then the down-heap bubbling is performed that is the elements are swapped
until the heap order property is maintained.
Time Complexity: O(log n)

Search: O(n)

Peek: O(1)
"""

class Heap:

    def __init__(self, heap=[]):
        if heap:
            self._heap = heap
            self._heapify(0)
        else:
            self._heap = []

    # Initializing Helper private methods

    def _parent(self, p):
        """Return parent index of node index p"""
        return (p - 1) // 2

    def _left_child(self, p):
        """Return left child index of node index p"""
        return (p*2) + 1

    def _right_child(self, p):
        """Return right child index of node index p"""
        return (p*2) + 2

    def _has_right_child(self, p):
        """Checks if the node index p has a right child"""
        return self._right_child(p) < len(self._heap)

    def _has_left_child(self, p):
        """Checks if the node index p has a left child"""
        return self._left_child(p) < len(self._heap)

    def _swap(self, i, j):
        """Swaps element of ith and jth position in the heap"""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _upheap(self, p):
        """
        Maintains the Heap Order Property by upheaping the value after
        insertion
        """
        parent = self._parent(p)
        # print('Element {} and Parent: {}'.format(self._heap[p], self._heap[parent]))

        if p > 0 and self._heap[parent] > self._heap[p]:

            self._swap(p, parent)
            self._upheap(parent)

    def _downheap(self, p):
        """
        Maintains the Heap Order Property by downheaping the value after
        deletion and swapping of values
        """
        if self._has_left_child(p):
            small_child = self._left_child(p)

            if self._has_right_child(p):
                small_child = self._right_child(p) if self._heap[self._right_child(p)] < self._heap[self._left_child(p)] else small_child

            if self._heap[p] > self._heap[small_child]:
                self._swap(p, small_child)
                self._downheap(small_child)

    def _heapify(self):
        pass


    # Overloading class methods
    def __len__(self):
        return len(self._heap)


    def __str__(self):
        return ' '.join(map(str, self._heap))


    # Heap Operations

    def insert(self, a):
        """
        Inserts the element into the heap
        """
        self._heap.append(a)
        self._upheap(len(self._heap) - 1)

    def delete_min(self):
        """
        Deletes the root element of the heap i.e the minimum value
        """
        if len(self._heap) ==  0:
            raise IndexError("The Heap is empty! Cannot delete an empty heap")

        self._swap(0, len(self._heap) -1)
        min_value = self._heap.pop()
        self._downheap(0)
        return min_value

    def peek(self):
        """Returns the minimum value of the heap but does not deletes it"""
        if len(self._heap) == 0:
            raise IndexError("The heap is empty! cannot peak an empty heap")
        return self._heap[0]
        
    def search(self, x, p=0):
        if self._heap[p] == x:
            return p
        if self._has_left_child(p):
            if x == self._heap[self._left_child(p)]:
                return self._left_child(p)
            self.search(self._left_child(p))
            if self._has_right_child(p):
                if x == self._heap[self._right_child(p)]:
                    return self._left_child(p)
                self.search(self._right_child(p))

        return -1
            
            


if __name__ == '__main__':
    heap = Heap()
    heap.insert(0)
    heap.insert(2)
    heap.insert(7)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    heap.insert(3)
    heap.insert(0)
    assert str(heap) == '0 0 3 1 5 7 6 2'
    assert heap.delete_min() == 0
    assert heap.delete_min() == 0
    assert str(heap) == '1 2 3 6 5 7'
    assert heap.peek() == 1
    print('Basic Tests Passed Successfully')
    print(heap)
    print(heap.search(6))
