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

    def __str__(self):
        return "{}, {}".format(self.key, self.value)



class BST:
    """
    Main BST implementation, will contains methods like insert, delete,
    search etc.

    Supported Methods:
    insert: inserts the key, value into the Binary Search Tree
    floor: Gets the floor value of the key into the Binary Search Tree
    delete: Delete the value from the binary search tree
    """

    def __init__(self):
        self.root = None


    def _floor(self, key, node):
        if not node:
            return
        elif node.key > key:
            return self._floor(key, node.left)

        right_node = self._floor(key, node.right)
        if right_node:
            return right_node
        else:
            return node

        
    def floor(self, key):
        """Gets the floor value of the key"""

        node =  self._floor(key, self.root)
        if not node:
            return False, -1, 1
        return node
        
    def _insert(self, node, key, value):
        """
        Helper insert method to make recursive calls for insertion in BST
        """
        if not node:
            return Node(key, value)
        elif node.key > key:
            node.left =  self._insert(node.left, key, value)
        elif node.key < key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node


    def insert(self, key, value=None):
        """ Method to insert the key, value into BST """
        self.root = self._insert(self.root, key, value)


    def _search(self, key, node):
        """Helper Search function that recursively searches for element"""
        if not node:
            return False, -1, -1

        if key == node.key:
            return True, node.key, node.value
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    def search(self, key):
        """ Search a specific key into the BST and return its value """
        if not self.root:
            return False, -1

        return self._search(key, self.root)


    def delete(self, key):
        """ Deletes a key from the BST """
        pass

    def _print_inorder(self, node):
        """Helper Print Function to print inorder binary tree"""
        if not node:
            return

        self._print_inorder(node.left)
        print(node.key, node.value)
        self._print_inorder(node.right)

    def print_inorder(self):
        """Prints the BST inorder manner"""
        self._print_inorder(self.root)
        


if __name__ == "__main__":
    a = [2, 9, 3, 5, 1, 7, 8]
    bst = BST()
    for v in a:
        bst.insert(v)
    bst.print_inorder()
    print(bst.floor(4))
    print(bst.search(2))
    print(bst.search(-1))
    
    
