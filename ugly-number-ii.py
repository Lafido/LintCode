class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            while  2 * ugly[i2] <= ugly[-1]: i2 += 1
            while  3 * ugly[i3] <= ugly[-1]: i3 += 1
            while  5 * ugly[i5] <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]