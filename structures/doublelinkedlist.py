"""
Double Linked List

It is a collection of linked nodes where every node has two pointers one for its previous
and one for its backwards.Adds elemement and removes at O(1)

Usage:
dll = DoubleLinkedList()
dll.add(1)
dll.add(2)
dll.add(3)
dll.printfwd()
print(f'Middle: {dll.middle.x}')
dll.add(4)
dll.add(5)
dll.add(6)
print(f'Middle: {dll.middle.x}')
print('Forward Print:')
dll.printfwd()
print('Backward Print:')
dll.printbwd()
dll.remove()
print(f'Middle: {dll.middle.x}')
dll.printfwd()
"""
class DoubleLinkedList:
    """
    Implementation of Doubly Linked List

    Methods:
    add: Adds a new element
    remove: removes the last element

    Additional Pointer of middle is also there for some competetive problem solving
    later I liked its idea and it is in the code still for fast half slicing
    """

    class Node:
        """
        Implementation of Node
        
        A node is the basic unit of any linked list, in case of doubly linked list
        the node has a next pointer as well as a previous pointer (prev)
        """
        def __init__(self, x=None):
            """
            Input:
            x : Value of the Node
            """
            self.x = x
            self.prev = None
            self.next = None

    def __init__(self):
        """
        This implementation has two empty Nodes one for head and other for tail
        which is the head and start of linked list and the value of these is None
        There is also a middle pointer.
        """
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.middle = self.head
        self.length = 0

    def add(self, x):
        """
        Adds the element to the end of list
        """
        new_node = self.Node(x)
        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.length += 1
        if self.length %2 == 0:
            self.middle = self.middle.next

    def remove(self):
        """
        Removes the element from the end of list
        """
        if self.length == 0:
            exit(1)
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.length -= 1
        if self.length % 2 != 0:
            self.middle = self.middle.prev

    def printfwd(self):
        """
        Uses the next pointer and prints the list in forward manner
        """
        iterator = self.head.next
        while iterator.next:
            print(iterator.x, end=' ')
            iterator = iterator.next
        print()

    def printbwd(self):
        """
        Uses the prev pointer and prints the list in backward manner
        """
        iterator = self.tail.prev
        while iterator.prev:
            print(iterator.x, end=' ')
            iterator = iterator.prev
        print()

if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.add(1)
    dll.add(2)
    dll.add(3)
    dll.printfwd()
    print(f'Middle: {dll.middle.x}')
    dll.add(4)
    dll.add(5)
    dll.add(6)
    print(f'Middle: {dll.middle.x}')
    print('Forward Print:')
    dll.printfwd()
    print('Backward Print:')
    dll.printbwd()
    dll.remove()
    print(f'Middle: {dll.middle.x}')
    dll.printfwd()
