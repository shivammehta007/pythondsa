"""
KMP String Matching Algorithm

Knuth-Morris-Pratt Algorithm is a linear time String matching algorithm.

Suppose you have a string T of length m and a substring P of length n
where the first few characters of P matches in some index but the next
one doesn't match, in that scenario the computation of the P can be stored
in a pi i.e a prefix function where from there it can be continued instead
of rechecking for equality from index 0 of substring P.

Time Complexity:
Best: O(n) # when the substring starts from index 0 of T
Average: O(n + m)
Worse: O(n + m)

Space Complexity: O(n)

```
>>> string = abxabcabcaby
>>> substring = abcaby
>>> KMP.search(string, substring)
True
```
"""


class KMP:
    """
    KMP

    Knuth Morris Pratth Algorithm
    """

    @staticmethod
    def compute_prefix_function(substring):
        """
        This methods computes the prefix function used to do string search
        :param: substring -> String
        :return: list -> Prefix function of substring
        """
        prefix = [0] * len(substring)
        j = 0
        i = 1
        while i < len(substring):
            if substring[i] != substring[j] and j > 0:
                j = prefix[j - 1]
                continue
            elif substring[i] != substring[j] and j == 0:
                prefix[i] = 0
                i += 1
                continue
            else:
                prefix[i] = j + 1
                j += 1
                i += 1

        return prefix

    @staticmethod
    def search(string, substring):
        """
        Checks for the presence of substring in the string
        :param: string  -> String to be searched in
        :param: substring -> Substring to be searched for
        :return: Boolean -> True if the substring is found else False
        """

        prefix = KMP.compute_prefix_function(substring)
        j = 0
        i = 0
        while i < len(string) and j < len(substring):
            if string[i] == substring[j]:
                j += 1
                i += 1
            else:
                if j == 0:
                    i = i + 1
                    continue
                j = prefix[j-1]

        if j == len(prefix):
            return True

        return False


if __name__ == '__main__':
    # Test case for compute prefix function
    TEST_CASE = 'aabaabaaa'
    assert KMP.compute_prefix_function(
        TEST_CASE) == [0, 1, 0, 1, 2, 3, 4, 5, 2]
    TEST_CASE = 'abcdabca'
    assert KMP.compute_prefix_function(
        TEST_CASE) == [0, 0, 0, 0, 1, 2, 3, 1]

    from random import randint

    for i in range(100):
        string = ''.join([chr(97 + randint(0, 26)) for _ in range(100)])
        substring = ''.join([chr((97) + randint(0, 26)) for _ in range(5)])
        assert (substring in string) == (KMP.search(string, substring))

    print("All test cases passed")
