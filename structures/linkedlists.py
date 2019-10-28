#!/bin/usr/env python3
"""
Implementation of liked lists in python3

TODO: Add Docstrings
"""


class LinkedList:
    """
    Class to Implement linked lists

    Linked lists keeps track of memory location of head and furthur elements
    and traversal is done in a sequence manner
    """
    class Node:
        """
        Subclass used to represent one data element aka Node

        Node has a value that holds its value and a next reference
        which refers to the next element in the sequence or None otherwise
        """
        def __init__(self, x):
            self.next = None
            self.value = x

    def __init__(self, x):
        node = self.Node(x)
        self.head = node
        self.tail = node
        self.size = 1
        self.errors = {'underflow': 'UnderFlow Error: Array is Empty',
                       'overflow': 'OverFlow Error: Array is full or' +
                                   ' reached maximmum size'}

    def __len__(self):
        return self.size

    def add_first(self, x):
        """
        Adds the element to the starting of the linked list
        """
        node = self.Node(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_last(self, x):
        """
        Adds the element to the end of the linked list
        """
        node = self.Node(x)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def print_it(self):
        """
        Traverses the list from start to end by pointing from one node to
        another
        """
        node = self.head
        print('Array : ', end=' ')
        while node:
            print(node.value, end=' ')
            node = node.next

    def add(self, x, position):
        """
        Adds the element to a specific location in the linked list
        """
        if position == 0:
            self.add_first(x)
            return

        if position > self.size:
            print(self.errors['overflow'])
            return
        if position == self.size-1:
            self.add_last(x)
            return

        i = 0
        node = self.head
        while node:
            i += 1
            if i == position:
                new_node = self.Node(x)
                new_node.next = node.next
                node.next = new_node
                self.size += 1
                break
            node = node.next

    def delete_first(self):
        """
        Deletes the first element or head element in the linked list
        """
        if self.size == 0:
            print(self.errors['underflow'])
        elif self.size > 1:
            self.head = self.head.next
            self.size -= 1
        else:
            self.head = None
            self.tail = None
            self.size -= 1

    def delete_by_position(self, position):
        """
        Deletes the element by position in the linked list
        """
        if self.size == 0:
            print(self.errors['underflow'])
        i = 0
        if position == 0:
            self.delete_first()
            return

        node = self.head
        while node:
            i += 1
            if i == position:
                node.next = node.next.next
                self.size -= 1
                if i == self.size-1:
                    self.tail = node
                break
            node = node.next

    def delete_by_value(self, value):
        """
        Deletes the element by value in the linked list
        """
        if self.size == 0:
            print(self.errors['underflow'])

        if self.head.value == value:
            self.delete_first()
            return

        node = self.head
        i = 0
        while node.next:
            i += 1
            if node.next.value == value:
                node.next = node.next.next
                self.size -= 1
                if i == self.size-1:
                    self.tail = node
                return
            node = node.next


if __name__ == '__main__':
    print('Initial List with 2')
    linked_lst = LinkedList(2)
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Adding 1 in first')
    linked_lst.add_first(1)
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Adding 4 in last')
    linked_lst.add_last(4)
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Adding 3 at index 2')
    linked_lst.add(3, 2)
    linked_lst.print_it()
    print(f'\tSize : {len(linked_lst)}')

    print('Deleting First')
    linked_lst.delete_first()
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Deleting by Position 1')
    linked_lst.delete_by_position(1)
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Delete by Value 4')
    linked_lst.delete_by_value(4)
    linked_lst.print_it()
    print(f'\t\tSize : {len(linked_lst)}')

    print('Printing Final Tail and Size')
    print(f'Head : {linked_lst.head.value}')
    print(f'Tail : {linked_lst.tail.value}')
    print(f'Size : {len(linked_lst)}')
