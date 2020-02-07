"""
Rabin Karp Algorithm for String Matching

The concept of rabin karp is hashing, if two values are same they will have
same hash values and same digits, so rabin karp first computes hashes and
if they match then it moves forward to check digits otherwise skips it.
Let assume was have a string P of length m and a substring S of length n
The hashes can be computed in O(m) time with the help of ROLLING HASHES,
here the hash values of most significant digit is substracted and that
of the next digit is added.

Time Complexity:
Best Case: O(m - n + 1)
Average Case: O(m + n)* amortized
Worst Case: O(mn)

Usage:
```
>>> RabinKarp.search('hello', 'll')
True
>> RabinKarp.search('qwerty', 'abcd')
False
```
"""


class RabinKarp:
    """
    Rabin Karp Algorithm
    """

    @staticmethod
    def get_value(char):
        """
        Returns value of character in decimal system where a =1, z=26
        :param: char -> integer
        :return: integer
        """
        return ord(char) - ord('a') + 1

    @staticmethod
    def check_digits(index, string, sub_string):
        """Checks for equal strings and substring from index of string"""
        return string[index:index+len(sub_string)] == sub_string

    @staticmethod
    def search(string, sub_string, prime=10**7, d=26):
        """
        Returns True if the substring is present
        int the string otherwise returns False
        :param: string -> string
        :param: sub_string -> string
        :param: prime -> a prime number, the larger the better
        :param: d -> number of digits possible in strings |#s|
        :return: Boolean
        """
        l_s = len(string)
        l_sub = len(sub_string)
        if l_s < l_sub:
            return False

        hash_sub = 0
        hash_t = 0

        for i in range(l_sub):
            hash_sub += (RabinKarp.get_value(sub_string[i])
                         * (d ** (l_sub - i - 1))) % prime
            hash_t += (RabinKarp.get_value(string[i])
                       * (d ** (l_sub - i - 1))) % prime

        if hash_sub == hash_t:
            if RabinKarp.check_digits(0, string, sub_string):
                return True

        for i in range(1, l_s - l_sub + 1):
            # Calculate Rolling Hash
            hash_t = (d * (hash_t - (RabinKarp.get_value(string[i - 1]) * d**(
                l_sub - 1))) + RabinKarp.get_value(string[i + l_sub - 1])) \
                % prime

            if hash_sub == hash_t:
                if RabinKarp.check_digits(i, string, sub_string):
                    return True
        return False


if __name__ == '__main__':
    assert RabinKarp.get_value('a') == 1, 'Check Get Value Method'
    assert RabinKarp.get_value('z') == 26, 'Check Get Value Method'

    assert RabinKarp.search('hello', 'll') is True, 'Check Search Method'
    assert RabinKarp.search(
        'abcdefghjikl', 'aa') is False, 'Check Search Method'

    from random import randint

    for i in range(100):
        string = ''.join([chr(97 + randint(0, 26)) for _ in range(100)])
        substring = ''.join([chr((97) + randint(0, 26)) for _ in range(5)])
        assert (substring in string) == (RabinKarp.search(
            string, substring)), 'Check Search Method'

    print("All test cases passed")
