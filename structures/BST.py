"""
Binary Search Trees

This datastructure is generally used to store dictionaries and priority queue.
This is because of the fact that all the basic operation like search, insert, delete etc. takes time equivalent to the height of the tree i.e O(log n)
in average.

Time Complexities:
Best Case: O(1) when looking for the centermost element
Average Case: O(log n)
Worst Case: O(n) when the tree is built in a way that the elements are chained
            (like in that of linked list {my analogy})

Note: So that we can use it as a symbol table I will return tuple
      of key, value pairs. You can modify and change it accordingly.
"""

class Node:
    """
    This class will be a basic unit of the BST datastructure.
    It will have four instance variables
    key: integer for the key
    value: incase to use this as a dictionary or symbol table this can be used
    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None



class BST:
    """
    Main BST implementation, will contains methods like insert, delete,
    search etc.
    """

    def __init__(self):
        self.root = None


    def _insert(self, node, key, value):
        """
        Helper insert method to make recursive calls for insertion in BST
        """
        if not node:
            return Node(key, value)
        elif node.key < key:
            root.left =  self._insert(node.left, key, value)
        elif node.key > key:
            root.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node


    def insert(self, key, value=None):
        """ Method to insert the key, value into BST """
        self.root = self._insert(self.root, key, value)
        

    def search(self, key, root=None):
        """ Search a specific key into the BST and return its value """
        if not self.root:
            return False, -1

        if not root:
            root = self.root
        if key == self.root.key:
            return True, self.root.value
        elif key < self.root.key:
            return self.search(key, self.left)
        else:
            return self.search(key, self.right)

    def delete(self, key):
        pass

    
