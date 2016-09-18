class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        count = 0
        for i in range(32):
            print(a, b)
            print(a&1, b&1)
            if a & 1 != b & 1:
                count += 1
            a >>= 1
            b >>= 1
        return count