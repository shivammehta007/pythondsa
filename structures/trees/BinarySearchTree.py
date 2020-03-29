"""
Binary Search Trees

This datastructure is generally used to store dictionaries and priority queue.
This is because of the fact that all the basic operation like search, insert, delete
etc. takes time equivalent to the height of the tree i.e O(log n)
in average.

Time Complexities:
Best Case: O(1) when looking for the centermost element
Average Case: O(log n)
Worst Case: O(n) when the tree is built in a way that the elements are chained
            (like in that of linked list {my analogy})

Deleteion in Binary Search Tree:
Average Case: O(root n) Because as more number of elements are inserted and then
              deleted it becomes more skewed toward right, because of this deletion
              where we add element of the right to a higher position


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

    def __init__(self, key, value=None, count=0):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.count = count

    @classmethod
    def copy_node(cls, node):
        """ Class Method to create node from another node """
        new_node = cls(node.key, node.value)
        new_node.right = node.right
        new_node.left = node.left
        new_node.count = node.count
        return new_node

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
            return -1, -1
        if node.key > key:
            return self._floor(key, node.left)

        right_node = self._floor(key, node.right)
        if right_node[0] > 0:
            return right_node[0], right_node[1]
        return node.key, node.value

    def floor(self, key):
        """Gets the floor value of the key"""

        return self._floor(key, self.root)

    def _insert(self, node, key, value):
        """
        Helper insert method to make recursive calls for insertion in BST
        """
        if not node:
            return Node(key, value, 1)

        if  node.key > key:
            node.left = self._insert(node.left, key, value)
        elif node.key < key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        node.count = self.size(node.left) + self.size(node.right) + 1
        return node


    def insert(self, key, value=None):
        """ Method to insert the key, value into BST """
        self.root = self._insert(self.root, key, value)


    def _search(self, key, node):
        """Helper Search function that recursively searches for element"""
        if not node:
            return -1, -1

        if key == node.key:
            return node.key, node.value
        if key < node.key:
            return self._search(key, node.left)

        return self._search(key, node.right)

    def search(self, key):
        """ Search a specific key into the BST and return its value """
        if not self.root:
            return -1, -1

        return self._search(key, self.root)

    def _get_min(self, node):
        """ Helper function that returns minimum from a node """
        if not node.left:
            return node

        return self._get_min(node.left)

    def get_min(self):
        """ Returns the minimum node of the BST"""
        if not self.root:
            raise IndexError("Empty Tree")

        return self._get_min(self.root)

    def delete_min(self):
        """ Deletes the minimum element from the tree """
        if not self.root:
            raise IndexError("Empty Tree")

        self._delete_min(self.root)

    def _delete_min(self, node):
        """ Deletes the minimum element from a node """
        if not node.left:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self.size(node.left) + self.size(node.right)
        return node

    def _delete(self, key, node):
        """ Helper function to delete a node from BST """
        if not node:
            return -1, -1

        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right

            temp = Node.copy_node(node)
            node = self.get_min(temp.right)
            node.right = self._delete_min(temp.right)
            node.left = temp.left

        node.count = self.size(node.left) + self.size(node.right) + 1

        return node

    def delete(self, key):
        """ Deletes a key from the BST"""
        self._delete(key, self.root)

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

    def size(self, node):
        """ Returns the count of the node """
        if not node:
            return 0
        return node.count

    def __len__(self):
        return self.size(self.root)

if __name__ == "__main__":
    # Test Code
    A = [2, 9, 3, 5, 1, 7, 8]
    B = [(2, "Two"), (9, "Nine"), (3, "Three"), (5, "Five")]
    BS = BST()
    for v in A:
        BS.insert(v)
    BS.print_inorder()
    print(BS.floor(4))
    print(BS.search(2))
    print(BS.search(-1))
    print("Length: {}".format(len(BS)))
    BS.delete(3)
    BS.print_inorder()
    print("Length: {}".format(len(BS)))

    BST2 = BST()
    for v, s in B:
        BST2.insert(v, s)

    BST2.print_inorder()
    print(BST2.floor(8))
    print(BST2.search(5))
    print(BST2.search(4))
    print("Length: {}".format(len(BST2)))
    BST2.delete(5)
    BST2.print_inorder()
    print("Length: {}".format(len(BST2)))
