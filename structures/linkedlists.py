#!/bin/usr/env python3
"""
Implementation of liked lists in python3

TODO: Add docstrings
"""


class LinkedList:
    class Node:
        def __init__(self, x):
            self.next = None
            self.value = x

    def __init__(self, x):
        self.head = self.Node(x)
        self.tail = self.head
        self.size = 1

    def add_first(self, x):
        node = self.Node(x)
        node.next = self.head
        self.head = node.next
        self.size += 1

    def add_last(self, x):
        self.tail = self.Node(x)
        self.size += 1

    def print_it(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


if __name__ == '__main__':
    linked_lst = LinkedList(1)
    linked_lst.add_first(5)
    linked_lst.add_last(2)
    linked_lst.print_it()
