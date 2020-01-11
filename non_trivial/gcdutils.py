"""
Euclidean Algorithm

It is used to calculate the GCD i.e Greatest Common Divisor for two numbers.
It can be extended to get coefficients
In Math the euclidean algorithm works like:
GCD(62, 16):
[62] = [16]*3 + [14]
Shifts the elements in brackets
[16] = [14]*1 + [2]
[14] =  [2] * 77 + [0]
Since remainder is 0 the second last remaindeer will be GCF
"""

class GCD:
    """
    GCD Utilities

    Contains Utilities for GCD its extended versions
    """

    @staticmethod
    def gcd(x, y):
        """
        Returns the GCD or also known as HCF of two numbers
        Parametrs:
        x: Integer
        y: Integer
        Returns: Integer
        """
        if x == 0:
            return y

        return GCD.gcd(y % x, x)


if __name__ == '__main__':
    assert GCD.gcd(62, 16) == 2
    assert GCD.gcd(4, 8) == 4
    assert GCD.gcd(11, 23) == 1
    print('Tests Passed Successfully')
    
