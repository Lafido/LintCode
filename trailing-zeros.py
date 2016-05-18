class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        tail = 0
        while n != 0:
            n /= 5
            tail = tail + n
        return tail
        