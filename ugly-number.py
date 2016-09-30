class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        while num != 1:
            temp = num
            if num % 2 == 0:
                num /= 2
            if num % 3 == 0:
                num /= 3
            if num % 5 == 0:
                num /= 5
            if num == temp:
                return False
        return True
