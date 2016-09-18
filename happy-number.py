class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        mid = []
        prior = n
        while n != 1:
            posterior = 0
            while n > 0:
                posterior += (n % 10) ** 2
                n = n // 10
            if posterior in mid:
                return False
            else:
                mid.append(posterior)
            n = posterior
        return True
