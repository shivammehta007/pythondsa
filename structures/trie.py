"""
Trie

Trie is a datastructure used to store strings for prefix matches or spell check
In trie every node has a hashmap of key of characters and value of reference to
another node.
Time Complexity:
Insertion of lexicon: O(l*n)
"""


class Trie:

    class _Node:

        def __init__(self, end=True):
            self.characters = {}
            self.end = end

    def __init__(self):

        self.root = self._Node()

    def add(self, string):
        for char in string:
