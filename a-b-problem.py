class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        if a == -b:
            return 0
        return a if b == 0 else self.aplusb(a ^ b,  (b & a) << 1)