class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        sign = 1 if n > 0 else -1
        result, n = 0, abs(n)
        while n != 0:
            if result > 214748364:
                return 0
            result = result * 10 + n % 10
            n /= 10
        return result * sign