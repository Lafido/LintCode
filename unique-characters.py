class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        num = 0
        for c in str:
            pos = ord(c)
            if (num >> pos) & 1 == 1:
                return False
            num |= 1 << pos
        return True