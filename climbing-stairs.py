class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 1 or n == 0:
            return 1
        if n == 2:
            return 2
        result, last = 2, 1

        for i in range(2, n):
            result = result + last
            last = result - last
        return result
