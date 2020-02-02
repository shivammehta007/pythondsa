"""
Permutation

This method is used to generate permutations of a string or an array.
It will return list of all possible combinations.
Runtime of this algorithm is O(N!)
Usage:
```
>>>from Permutation import permute
>>>permute('AB')
[['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], 
['C', 'A', 'B'], ['C', 'B', 'A']]
```
"""
class Permutation:
    """
    Permutation Class
    """
    @staticmethod
    def permute(current, fixed_prefix=[], results=[]):
        """
        Permutes string adn arrau"
        """
        if not current:
            return results.append(fixed_prefix)

        if isinstance(current, str):
            current = [x for x in current]
        for i, V in enumerate(current):
            next_array = current[:i] + current[i+1:]
            Permutation.permute(next_array, fixed_prefix + [V], results)

        return results



if __name__ == '__main__':
    from itertools import permutations
    from random import randint
    N = randint(2, 10)
    TESTING_ARRAY = [randint(1, 100) for x in range(N)]
    assert Permutation.permute(TESTING_ARRAY) == list(map(list, permutations(TESTING_ARRAY)))
    print("Elementary Test Casses passed")
