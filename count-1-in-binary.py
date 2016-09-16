class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        for _ in range(32):
            count += num & 0x1
            num = num >> 1
        return count
