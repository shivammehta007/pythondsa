"""
Trie

Trie is a datastructure used to store strings for prefix matches or spell check
In trie every node has a hashmap of key of characters and value of reference to
another node.
Time Complexity:
Insertion of lexicon: O(l*n) -> l is length of key and n is number of words
Searching/Insertion: O(l) -> l is length of key

Space Complexity: O(z*l*n) -> z is alphabet length, l is length of key,
                    n is number of words

"""


class Trie:
    """
    Trie

    Trie is a treelike datastructure used to predict suggestion here is a
    simple implementation of it with add and search functionality.

    It has a root that is the head or the Trie and a node_count to count
    total number of nodes currently in Trie
    """

    class _Node:
        """
        Node

        This is how a trie node looks like it has a hashmap of characters
        with an end indicating weather this is the end of word or not.
        One additional field that I added is the frequency count just for
        furthur probabilistic calculations if required.
        """

        def __init__(self, end=False):
            self.characters = {}
            self.frequency = 0
            self.end = end

    def __init__(self):
        self.root = self._Node()
        self.node_count = 1

    def add_string(self, string):
        """
        Adds a string to the trie
        Parameters:
        string: String
        """
        node = self.root
        for c in string:
            if c not in node.characters:
                node.characters[c] = self._Node()
                self.node_count += 1

            node = node.characters[c]
            node.frequency += 1

        node.end = True

    def search_word(self, string):
        """
        Searches for a word in the trie
        Parameters:
        string: String
        """
        node = self.root
        for c in string:
            if c not in node.characters:
                return False
            node = node.characters[c]

        if node.end:
            return True

        return False


if __name__ == '__main__':
    T = Trie()
    T.add_string('cat')
    T.add_string('dog')
    T.add_string('camel')
    assert T.node_count == 10
    assert T.search_word('cat')
    assert T.search_word('dog')
    assert T.search_word('camel')
    assert not T.search_word('cab')
    print('Test Passed Successfully')
